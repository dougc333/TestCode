% Copyright 2011 Zdenek Kalal
%
% This file is part of TLD.

function tld = tldProcessFrame(tld,i)

I = tld.source.idx(i); % get current index
tld.img{I} = img_get(tld.source,I); % grab frame from camera / load image

% TRACKER  ----------------------------------------------------------------

[tBB tConf tValid tld] = tldTracking(tld,tld.bb(:,I-1),I-1,I); % frame-to-frame tracking (MedianFlow)

% DETECTOR ----------------------------------------------------------------

[dBB dConf tld] = tldDetection(tld,I); % detect appearances by cascaded detector (variance filter -> ensemble classifier -> nearest neightbour)
%dBB = [];
% INTEGRATOR --------------------------------------------------------------

DT = 1; if isempty(dBB), DT = 0; end % is detector defined?
TR = 1; if isempty(tBB), TR = 0; end % is tracker defined?

%keyboard;

%% -------------------------------------- (BEGIN) --------------------------
%% TODO: We have provided a strategy to fuse the detection results
%%       with the tracker. This is a very simple method which is slightly
%%       different from the original TLD tracker. You should play
%%       around with different ways of combining the detector and tracker.
%%       Choosing a good startegy will greatly improve performance.


if TR % if tracker is defined
    
    % copy tracker's result
    tld.bb(:,I)  = tBB;
    tld.conf(I)  = tConf;
    tld.size(I)  = 1;
    tld.valid(I) = tValid;
    
    if DT % if detections are also defined
        
        [cBB,cConf,cSize] = bb_cluster_confidence(dBB,dConf); % cluster detections
        id = bb_overlap(tld.bb(:,I),cBB) < 0.5 & cConf > tld.conf(I); % get indexes of all clusters that are far from tracker and are more confident then the tracker
        
        if sum(id) == 1 % if there is ONE such a cluster, re-initialize the tracker
            
            tld.bb(:,I)  = cBB(:,id);
            tld.conf(I)  = cConf(:,id);
            tld.size(I)  = cSize(:,id);
            tld.valid(I) = 0; 
            
        else % othervide adjust the tracker's trajectory
            
            idTr = bb_overlap(tBB,tld.dt{I}.bb) > 0.7;  % get indexes of close detections
            tld.bb(:,I) = mean([repmat(tBB,1,10) tld.dt{I}.bb(:,idTr)],2);  % weighted average trackers trajectory with the close detections
            
        end
    end
    
else % if tracker is not defined
    if DT % and detector is defined
        
        [cBB,cConf,cSize] = bb_cluster_confidence(dBB,dConf); % cluster detections
        
        if length(cConf) == 1 % and if there is just a single cluster, re-initalize the tracker
            tld.bb(:,I)  = cBB;
            tld.conf(I)  = cConf;
            tld.size(I)  = cSize;
            tld.valid(I) = 0; 
            fprintf('Re-initializing tracker ... \n');
        end
    end
end

%% ------------------------------------- (END) ----------------------------


% LEARNING ----------------------------------------------------------------

if isnan(sum(tld.bb(:, I)))
  fprintf('Box lost ... \n');
end


if tld.control.update_detector && tld.valid(I) == 1
    tld = tldLearning(tld,I);
end

% display drawing: get center of bounding box and save it to a drawn line
if ~isnan(tld.bb(1,I))
    tld.draw(:,end+1) = bb_center(tld.bb(:,I));
    if tld.plot.draw == 0, tld.draw(:,end) = nan; end
else
    tld.draw = zeros(2,0);
end

if tld.control.drop_img && I > 2, tld.img{I-1} = {}; end % forget previous image








