$(document).ready(function () {


        /*************************************************************************
	* Add CAN-296: Instructors need to see their past courses under Import Course Content by default *
	*************************************************************************/
       var currentCoursePath = window.location.pathname;
       var courseCopyContentImportPattern = /(\/courses\/[0-9]+\/content_migrations)$/i;
       if (courseCopyContentImportPattern.test(window.location.pathname))
       {
        setTimeout(function()
        {
           $('#chooseMigrationConverter').change(function() {
                if ($(this).val()=="course_copy_importer")
                {
                   setTimeout(function()
                   {
                        if ($('#include_completed_courses').length)
                        {
                            if ( !$('#include_completed_courses').prop( "checked"))
                            {
                                $('#include_completed_courses').prop( "checked", true );
                                $('#include_completed_courses').click();
                            }
                        }
                    }, 500);
                }
            });
        }, 500);
       }
       //end of CAN-296*************************************************************************/




        /*************************************************************************
	 * Add CAN-280: Hide Batch Update option in SIS Import page *
	 **************************************************************************/
        if (window.location.href.indexOf("sis_import") > -1)
        {
           $('#batch_check').css("display", "none");
        }
	/*************************************************************************
	 * End of  CAN-280
	 **************************************************************************/


	/*************************************************************************
	 * Add CAN-166: Add warning to SpeedGrader about multiple graders working at same time *
	 **************************************************************************/
	if (window.location.href.indexOf("speed_grader") > -1) {
		var displayMessage = '<div class="ic-flash-error" style="top:20px" id="speedgrader-warning"><div class="ic-flash__icon" aria-hidden="true"><i class="icon-warning"></i></div><b>AVOID DATA LOSS</b>: Multiple graders should not grade the same assignment at the same time.<br /><br /><a href="https://canvashelp.stanford.edu/hc/en-us/articles/115007357988-Warning-about-multiple-graders-using-SpeedGrader">Click here to learn more about avoiding data loss.</a><br /><br /><a href="javascript:void(0);" id="xModalNoShow">Don\'t show this message again in this course.</a><button type="button" class="Button Button--icon-action close_link" onClick="javascript:$(\'#speedgrader-warning\').hide();"><i class="icon-x" aria-hidden="true"></i><span class="screenreader-only">Close</span></button></div>';

		//Check cookie exists
		if ($.cookie('xSpeedGModal') != null) {
			//Cookie exists, read it

			//Set array
			var cIds = JSON.parse($.cookie('xSpeedGModal'));

			//Check current course against the array of courses
			if ($.inArray(ENV["course_id"], cIds) < 0) {
				$('#flash_message_holder').prepend(displayMessage);
			}
		} else {
			//Cookie doesnt exist, show message
			$('#flash_message_holder').prepend(displayMessage);
		}

		//Write to cookie
		$('#xModalNoShow').on('click', function () {
			if ($.cookie('xSpeedGModal') == null) {
				//Set cookie
				var cIds = [ENV["course_id"]];

				//$.cookie('xSpeedGModal', JSON.stringify(cIds));
				$.cookie('xSpeedGModal', JSON.stringify(cIds), {
					path: '/',
					expires: 365
				});
			} else {
				//append to arr and reset cookie
				var cIds = JSON.parse($.cookie('xSpeedGModal'));

				cIds.push(ENV["course_id"]);

				//$.cookie('xSpeedGModal', JSON.stringify(cIds));
				$.cookie('xSpeedGModal', JSON.stringify(cIds), {
					path: '/',
					expires: 365
				});
			}

			$('#speedgrader-warning').hide();
		});
	}

	//End CAN-166

	/*************************************************************************
	 * CAN-223 Make it easier to find All Courses page
	 **************************************************************************/
   if (window.location.pathname == "/") {
     setTimeout(function()
     {
       if ($("h1.ic-Dashboard-header__title").length == 1) {
         $("h1.ic-Dashboard-header__title").after('<a href=\"/courses\" class=\"Button button-sidebar-wide\">View All Courses</a>');
       }
     }, 500);
   }

	/*************************************************************************
	 * CAN-201 Add Course Unpublished warning to home page
	 **************************************************************************/

	if ($(".ui-button.disabled.btn-unpublish").length == 1) {
		$('#content-wrapper').prepend('<div align="center" style="margin-bottom:10px; background-color:#edd; border:2px solid #a44; border-radius:5px; padding:5px;">  \
  <p>This course is not published. Students cannot access the course and notifications will not be sent.</p>  \
  <div align="center" > \
  <form action=""> \
  <input type="button" class="btn" id="stanford_home_warning_publish" value="Publish Course"> \
  </form> \
  </div></div>');
	} else {
		// do nothing
	}

	$("#stanford_home_warning_publish").click(function () {
		$('#course_status_form').find(":submit").click()
	});

	/*************************************************************************
	 * CAN-202 Add warning in Announcements about lack of notifications for unpublished course
	 **************************************************************************/

	if ($(".announcements.active").length == 1) {
		var url = "https://" + window.location.host + "/api/v1/courses/" + ENV["COURSE_ID"];
		var homeurl = "https://" + window.location.host + "/courses/" + ENV["COURSE_ID"];
		$.ajax(url, {
			statusCode: {
				// status will be 200 if the namespace custom data does exist
				200: function (response) {
					if (response.workflow_state == "unpublished") { //checks to make sure that the data value is indeed true
						$('#content-wrapper').prepend('<div align="center" style="margin-bottom:10px; background-color:#edd; border:2px solid #a44; border-radius:5px; padding:5px;">  \
            <p>Notifications will not be sent for any announcements posted before the course is published.</p> \
            <div align="center"> \
            <form action=""> \
            <input type="button" class="btn" id="stanford_annc_warning_publish" value="Publish Course">  \
            </form> \
            </div> \
            </div>');

						$("#stanford_annc_warning_publish").click(function () {
							var publishurl = "https://" + window.location.host + "/api/v1/courses/" + ENV["COURSE_ID"];

							$.ajax({
								url: publishurl,
								type: "PUT",
								data: "course[event]=offer",
								statusCode: {
									200: function (response) {
										location.reload();
									}
								}
							});
						});
					} else {
						// to nothing
					}
				}
			}
		});
	}

	//End CAN-201/202


       /*************************************************************************
    	 * Begin of CAN-242 As an instructor or TA, I would like an easier way to post or update a syllabus file to the Syllabus tool
    	 **************************************************************************/
        if($('.edit_syllabus_link').length>0 )
        {

            if (ENV.SYLLABUS_BODY.length>0 )
            {
                var regexpFile=/^(<p>)?<a(.*?)class="instructure_file_link instructure_scribd_file"(.*?)<\/a>(<\/p>)?$/;
                var regexpFile1=/<\/a>/g;
                var testFile = regexpFile.test(ENV.SYLLABUS_BODY);

                if (testFile==false || (ENV.SYLLABUS_BODY).match(regexpFile1).length>1)
                    return;
            }


            var stanford_syl_course_id = ENV.context_asset_string.split('_')[1];
/*
            var ALL_GDB_ACCOUNTS = [11,215,216,217,218,219,220,221,222,223,224,253,306,237];
            var courseWithAccountID = getCourseAccount();
            console.log("account_id from getCourseAccount result json: " + courseWithAccountID.account_id);
            var courseAccountID = courseWithAccountID.account_id==null?0:courseWithAccountID.account_id;

            if(ALL_GDB_ACCOUNTS.includes(courseAccountID))
                return;
*/
            // Variable to store your files
            var stanford_upload_file;
            var stanford_syl_syllabus_body ="";
            var stanford_syl_courseFileList = [];
            var stanford_syl_courseFileListULTag;
            var syllabusTagInnerHTML;
            var stanford_syl_selectedUsuageRight="own_copyright";
            var stanford_syl_uploaded_file = "";
            var stanford_syl_root_folder_id;

            var fileToolURL = "https://" + window.location.host + "/courses/" + stanford_syl_course_id + "/files";
            var settingToolURL = "https://" + window.location.host + "/courses/" + stanford_syl_course_id + "/settings";
            syllabusTagInnerHTML = ' \
              <div id="stanford_syl_custom_div">  \
                <div id="stanford_syl_file_list_div"> \
                    <p id="stanford_syl_uploaded_file_p"></p> \
                    <div style="display:block" id="stanford_syl_add_file_replace_div"> \
                       <form action=""> \
                         <input type="button" class="btn" id="stanford_syl_add_file_replace_btn" value="Replace with a new file">  \
                       </form> \
                   </div> \
                    <div id="stanford_syl_edit_file_replace_div" style="display:block"> \
                       <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OR</p> \
                       <form action=""> \
                          <input type="button" class="btn" id="stanford_syl_edit_replace_btn" value="Add multiple files, inline text, or embedded media">  \
                       </form> \
                       <p>NOTE:&nbsp;&nbsp;The file that\'s being replaced can still be found under <a href='+fileToolURL+'>Files</a> where all of your course files reside.</P> \
                    </div> \
                </div> \
                <div style="display:block" id="stanford_syl_add_file_div"> \
                   <form action=""> \
                     <input type="button" class="btn" id="stanford_syl_add_file_btn" value="Add a single file only">  \
                   </form> \
                </div>\
                <div id="stanford_syl_edit_file_div" style="display:block"> \
                   <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OR</p> \
                   <form action=""> \
                     <input type="button" class="btn" id="stanford_syl_edit_btn" value="Add multiple files, inline text, or embedded media">  \
                   </form> \
                   <p></p><p></p><p></p> \
                   <p>NOTE:  Syllabus content posted to Canvas will be available at <a href="http://syllabus.stanford.edu">http://syllabus.stanford.edu</a>. <br> \
                   This will happen even if your Canvas site is unpublished or if your course has concluded.</p> \
                   <p></p> \
                   <p>Additionally, anyone at Stanford visiting <a href="http://syllabus.stanford.edu">http://syllabus.stanford.edu</a> will be able to view your course\'s syllabus content unless you choose otherwise. </p> \
                   <p></p> \
                   <p>To restrict syllabus content access to only members of your course:</p> \
                   <ul> \
                     <li>go to <a href='+settingToolURL+'>Settings</a> located at the bottom of the course navigation bar</li> \
                     <li>on the Course Details tab, locate the Visibility section. Select Course for Syllabus</li> \
                     <li>click Update Course Details when done</li> \
                   </ul>  \
                </div> \
              </div>';

            $("#course_syllabus_details").css("display", "none");
            $('#course_syllabus').append(syllabusTagInnerHTML);



            if (ENV.SYLLABUS_BODY.length>0 )
            {
                $('#stanford_syl_add_file_div').css("display", "none");
                $('#stanford_syl_edit_file_div').css("display", "none");
            }
            else
            {
                $('#stanford_syl_add_file_replace_div').css("display", "none");
                $('#stanford_syl_edit_file_replace_div').css("display", "none");
            }

        }


        function getCourseAccount()
        {
            //Course - GET https://canvas.stanford.edu:443/api/v1/courses/20973?include[]=syllabus_body
            var location="https://" + window.location.host + "/api/v1/courses/" + stanford_syl_course_id;
            var result = "";
            $.ajax({
                type: "get",
                data: "",
                url: location,
                //line added to get ajax response in sync
                async: false,
                success: function(data) {
                    result = data;
                },
                error: function() {
                }
            });
            console.log("getCourseAccount result json: " + JSON.stringify(result));
            return result;
        }


        $(document).on('click', '#stanford_syl_addfile_mycomputer_upload_btn', function()
        {
            $("#stanford_syl_addfile_mycomputer_upload").focus().click();
    	});


        $(document).on('click', '#stanford_syl_edit_btn', function()
        {
             $('.edit_syllabus_link').click();
    	});


         $(document).on('click', '#stanford_syl_edit_replace_btn', function()
         {
             $('.edit_syllabus_link').click();
    	 });


        $('.edit_syllabus_link').click(function ()
        {
          /*
            if ($('#stanford-syl-18').length)
            {
                // do nothing
            } else
            {
                $('#edit_course_syllabus_form').prepend('<div id="stanford-syl-18" style="background-color: #f5f5f5; border: 1px solid #A5AFB5; padding: 1px 5px 1px 10px; margin-bottom:10px;"><p>To upload a syllabus file,  click the <strong>Files</strong> tab on the right sidebar. Then, click <strong>Upload a new file</strong>.<br> When updating syllabus content, don&#39;t forget to click the <strong>Update Syllabus</strong> button.</p></div>');
            }
            */

            var syllabusBody = getSyllabusBody();
            console.log("syllabus_body from getSyllabusBody result json: " + syllabusBody.syllabus_body);
            var syllabusBodyEdit = syllabusBody.syllabus_body==null?"":syllabusBody.syllabus_body;
            console.log("syllabusBodyEdit: " + syllabusBodyEdit);

            setTimeout(function()
            {
                tinymce.EditorManager.activeEditor.setContent(syllabusBodyEdit);
                //tinymce.EditorManager.activeEditor.focus();
            }, 500);

        });



        function clearDialog()
        {
            stanford_upload_file = null;

            $('input[name=stanford_syl_addfile_radio][value=myComputer]').prop("checked",true)

            if($('#stanford_syl_addfile_mycomputer_upload').length)
            {
                $('#stanford_syl_addfile_mycomputer_upload').val('');
            }

            if($('#stanford_syl_addfile_myconputer_div').length)
            {
                $('#stanford_syl_addfile_myconputer_div').css("display", "block");
            }

            if($('#stanford_syl_addfile_myconputer_filename_span').length)
            {
                $("#stanford_syl_addfile_myconputer_filename_span").html("&nbsp;&nbsp;No file chosen");
            }


            if($('#stanford_syl_addCoursefilenote_div').length)
            {
                $('#stanford_syl_addCoursefilenote_div').remove();
            }

            if($('#stanford_syl_addCoursefile_div').length)
            {
                $('#stanford_syl_addCoursefile_div').remove();
            }

            if($('#stanford_syl_addfile_dialog_copyright_sel').length)
            {
                $('#stanford_syl_addfile_dialog_copyright_sel').remove();
            }

            $('#stanford_syl_addfile_dialog_add').css("display", "inline-block");
        }


        $(document).on('click', '.stanford_syl_addfile_radio', function()
        {
            var stanfordSylAddfileRadioVal = $('input[name=stanford_syl_addfile_radio]:checked', '#stanford_syl_addfile_radio_form').val();

            if (stanfordSylAddfileRadioVal=='myComputer')
            {
                $('#stanford_syl_addfile_dialog_add').css("display", "inline-block");

                if (stanford_upload_file==null)
                {
                    $("#stanford_syl_addfile_dialog_add").button("option", "disabled", true);
                }
                else
                {
                    $("#stanford_syl_addfile_dialog_add").button("option", "disabled", false);
                }

                if($('#stanford_syl_addCoursefilenote_div').length)
                {
                    $('#stanford_syl_addCoursefilenote_div').remove();
                }

                if($('#stanford_syl_addCoursefile_div').length)
                {
                    $('#stanford_syl_addCoursefile_div').remove();
                }

                if($('#stanford_syl_addfile_myconputer_div').length)
                {
                    $('#stanford_syl_addfile_myconputer_div').css("display", "block");
                }
            }
            else //myCourseFiles
            {
                if($('#stanford_syl_addfile_myconputer_div').length)
                {
                    $('#stanford_syl_addfile_myconputer_div').css("display", "none");
                }

                stanford_syl_courseFileList = getCourseFileList();
                var stanford_syl_courseFolderList =  getCourseFileFolderList();
                var stanford_syl_courseFileAndFolderList = [];

                if (stanford_syl_courseFolderList.length >0)
                {
                    $.each(stanford_syl_courseFolderList , function(index, val)
                    {
                         if (val.parent_folder_id == null)
                             stanford_syl_root_folder_id=val.id;

                         stanford_syl_courseFileAndFolderList.push({
                            'id': val.id,
                            'parent_folder_id': val.parent_folder_id,
                            'is_folder': true,
                            'name': val.name
                          });
                    });
                }

                if (stanford_syl_courseFileList.length >0)
                {
                    $.each(stanford_syl_courseFileList , function(index, val) {
                         stanford_syl_courseFileAndFolderList.push({
                            'id': val.id,
                            'parent_folder_id': val.folder_id,
                            'is_folder': false,
                            'name': val.display_name
                          });
                    });
                }

                console.log("stanford_syl_courseFileAndFolderList:  " +JSON.stringify(stanford_syl_courseFileAndFolderList));
                console.log("stanford_syl_root_folder_id:  " +stanford_syl_root_folder_id);

                $('#stanford_syl_addfile_dialog_add').css("display", "none");


                var stanford_syl_addCoursefilenote_div;
                var stanford_syl_addCoursefile_div_html;
                var courseFileLisTag;
                if (stanford_syl_courseFileAndFolderList.length >0)
                {
                    stanford_syl_addCoursefilenote_div = '<div id="stanford_syl_addCoursefilenote_div" style="margin-bottom:10px; background-color:#edd; border:2px solid #a44; border-radius:5px; padding:5px;">Make sure that the file you select is published. Otherwise, students cannot access it.</div>';

                    stanford_syl_addCoursefile_div_html = '<button style="border: none; padding: 0; background: none" id="stanford_syl_addCoursefile_btn" class="stanford_syl_addCoursefile_btn" aria-expanded="true"> \
                        <svg name="IconMiniArrowDown" viewBox="0 0 1920 1920" rotate="0" width="1em" height="1em" aria-hidden="true" \
                        role="presentation" focusable="false" class="fTsnK_bGBk fTsnK_eXrk bHbtJ_bGBk" data-cid="InlineSVG SVGIcon"><g role="presentation"> \
                        <path d="M994.034 1226.26c-18.796 27.296-49.269 27.3-68.067 0L574.893 716.424C556.096 689.128 567.713 667 600.852 667h718.297c33.133 0 44.757 22.125 25.959 49.424L994.034 1226.26z" \
                        fill-rule="evenodd" stroke="none" stroke-width="1"></path></g></svg> <svg name="IconFolder" viewBox="0 0 1920 1920" \
                        rotate="0" width="1em" height="1em" aria-hidden="true" role="presentation" focusable="false" class="fTsnK_bGBk fTsnK_eXrk bHbtJ_bGBk bHbtJ_owrh" \
                       data-cid="InlineSVG SVGIcon"><g role="presentation"> \
                      <path d="M1807.059 1637.706c0 31.172-25.412 56.47-56.47 56.47H169.411c-31.06 0-56.47-25.298-56.47-56.47V225.94h590.907L854.4 451.824H225.882v112.94H1807.06v1072.942zM990.269 451.824L764.385 113H0v1524.706c0 93.402 76.01 169.412 169.412 169.412h1581.176c93.403 0 169.412-76.01 169.412-169.412V451.824H990.268z" \
                      fill-rule="evenodd" stroke="none" stroke-width="1"></path></g></svg> course files</button>';

                    courseFileLisTag= $("<div>", {html: stanford_syl_addCoursefile_div_html, class: '_mtenas', id:'stanford_syl_addCoursefile_div', style:'max-height: 37em;'});

                    courseFileLisTag.append(buildStanfordSylNestedFolderList(stanford_syl_courseFileAndFolderList, stanford_syl_root_folder_id) );
                }

                $(".stanford_syl_addfile_dialog").append(stanford_syl_addCoursefilenote_div);
                $(".stanford_syl_addfile_dialog").append(courseFileLisTag);
                console.log("courseFileLisTag:  " +courseFileLisTag.html());
            }

    	});


        function buildStanfordSylNestedFolderList(treeNodes, rootId)
        {
            var nodesByParent = {};

            $.each(treeNodes, function(i, node)
            {
                if (!(node.parent_folder_id in nodesByParent))
                    nodesByParent[node.parent_folder_id] = [];

                nodesByParent[node.parent_folder_id].push(node);
            });

            console.log(JSON.stringify(nodesByParent));

            function buildTree(children)
            {
                var $container = $("<ul class='stanford_syl_addCoursefile_ui' style='display:block; margin: 0px 0px 0px 0.8em !important; padding: 0px 0px 0px 0.2em !important; border-left: 1px dotted rgb(204, 204, 204) !important; flex: 1 1 0% !important; list-style: outside none none !important'>");

                if (!children) return;

                if(children[0].parent_folder_id!=stanford_syl_root_folder_id)
                {
                    $container.css("display", "none");
                    //console.log(JSON.stringify(children));
                }


                $.each(children, function(i, child)
                {
                    if(child.is_folder)
                    {
                        var divTagText = '<button style="border: none; padding: 0; background: none" id="stanford_syl_addCoursefile_btn" class="stanford_syl_addCoursefile_btn" aria-expanded="false"> \
                                <svg name="IconMiniArrowDown" viewBox="0 0 1920 1920" rotate="0" width="1em" height="1em" aria-hidden="true" \
                                role="presentation" focusable="false" class="fTsnK_bGBk fTsnK_eXrk bHbtJ_bGBk" data-cid="InlineSVG SVGIcon"><g role="presentation"> \
                                <path d="M994.034 1226.26c-18.796 27.296-49.269 27.3-68.067 0L574.893 716.424C556.096 689.128 567.713 667 600.852 667h718.297c33.133 0 44.757 22.125 25.959 49.424L994.034 1226.26z" \
                                fill-rule="evenodd" stroke="none" stroke-width="1"></path></g></svg> <svg name="IconFolder" viewBox="0 0 1920 1920" \
                                rotate="0" width="1em" height="1em" aria-hidden="true" role="presentation" focusable="false" class="fTsnK_bGBk fTsnK_eXrk bHbtJ_bGBk bHbtJ_owrh" \
                                data-cid="InlineSVG SVGIcon"><g role="presentation"> \
                                <path d="M1807.059 1637.706c0 31.172-25.412 56.47-56.47 56.47H169.411c-31.06 0-56.47-25.298-56.47-56.47V225.94h590.907L854.4 451.824H225.882v112.94H1807.06v1072.942zM990.269 451.824L764.385 113H0v1524.706c0 93.402 76.01 169.412 169.412 169.412h1581.176c93.403 0 169.412-76.01 169.412-169.412V451.824H990.268z" \
                               fill-rule="evenodd" stroke="none" stroke-width="1"></path></g></svg>'+child.name +'</button>';

                        $("<li>", {class: '_1bxohph'})
                            .appendTo($container)
                            .append( $("<div>", {html: divTagText, class: '_1bxohph'}).append(buildTree(nodesByParent[child.id]) ) );
                    }
                    else
                    {
                        var liTagText ='<button value="'+child.id+'" style="border: none; padding: 0; background: none" class="stanford_syl_addCoursefile_li_btn"><svg name="IconDocument" viewBox="0 0 1920 1920" rotate="0" width="1em" \
                                 height="1em" aria-hidden="true" role="presentation" focusable="false" class="fTsnK_bGBk fTsnK_eXrk bHbtJ_bGBk bHbtJ_owrh" \
                                 data-cid="InlineSVG SVGIcon"><g role="presentation"> \
                                 <path d="M1706.235 1807.059H350.941V112.94h903.53v451.765h451.764v1242.353zm-338.823-1670.74l315.443 315.447h-315.443V136.32zm402.182 242.487L1440.372 49.58C1408.296 17.62 1365.717 0 1320.542 0H238v1920h1581.175V498.635c0-45.176-17.618-87.755-49.58-119.83zM576.823 1242.353h790.589v-112.94H576.823v112.94zm0-451.765h903.53V677.647h-903.53v112.941zm0 677.647h451.765v-112.941H576.823v112.941zm0-451.764h677.648V903.53H576.823v112.941zm0-451.765h451.765V451.765H576.823v112.941z" \
                                 fill-rule="evenodd" stroke="none" stroke-width="1"></path></g></svg>'+child.name+'</button>';

                        $("<li>", {html: liTagText, class: '_1bxohph'})
                            .appendTo($container)
                            .append( buildTree(nodesByParent[child.id]) );
                    }
                });

                return $container;
            }

            return buildTree(nodesByParent[rootId]);
        }


        function getCourseFileList()
        {
            //Files - List files GET /v1/courses/{$course_id}/files
            var location="https://" + window.location.host + "/api/v1/courses/" + stanford_syl_course_id + "/files?per_page=100" ;
            var result = false;
            $.ajax({
                type: "get",
                data: "",
                url: location,
                //line added to get ajax response in sync
                async: false,
                success: function(data) {
                    result = data;
                },
                error: function() {
                }
            });
            console.log("getCourseFileList:  " +JSON.stringify(result));
            return result;
        }


        function getCourseFileFolderList()
        {
            //Files - List all folders GET /v1/courses/{$course_id}/folders
            var location="https://" + window.location.host + "/api/v1/courses/" + stanford_syl_course_id + "/folders?per_page=100" ;
            var result = false;
            $.ajax({
                type: "get",
                data: "",
                url: location,
                //line added to get ajax response in sync
                async: false,
                success: function(data) {
                    result = data;
                },
                error: function() {
                }
            });
            console.log("getCourseFileFolderList:  " +JSON.stringify(result));
            return result;
        }


        $(document).on('click', '#stanford_syl_addCoursefile_btn', function()
        {

            var stanfodSylFileListchildUl = $(this).siblings("ul.stanford_syl_addCoursefile_ui");

            if (stanfodSylFileListchildUl.css('display') == 'block')
            { // expend filder
                stanfodSylFileListchildUl.css('display', 'none');
            }
            else
            { // close the folder
                stanfodSylFileListchildUl.css('display', 'block');
            }
        });


        $(document).on('click', '.stanford_syl_addCoursefile_li_btn', function()
        {
            var selectedFileName;
            var selectedFileID = $(this).val();
            var selectedFileUrl;

            $.each(stanford_syl_courseFileList , function(index, val) {
                if (selectedFileID == val.id)
                {
                    selectedFileUrl = val.url;
                    selectedFileName = val.display_name;
                }
            });

            var fileJustUploaded = {
                fileName: selectedFileName,
                url: selectedFileUrl
            };

            syl_upload_to_syllabus(fileJustUploaded);

            clearDialog();

            $(".stanford_syl_addfile_dialog").dialog('close');
        });



        function syl_uploadfile_mycomputer_add(fileUploaded)
        {
           var courseRootFolder = getCourseRootFolderID();
           console.log("Course file root folfer id: " +JSON.stringify(courseRootFolder[0].id));
           var fileUploadArgs = {
    							"name" : fileUploaded.name,
                                "size" : fileUploaded.size,
                                "parent_folder_id" : courseRootFolder[0].id,
                                "on_duplicate" : "rename",
                                //"content_type" : "text/plain"
                                };
            console.log("Upload file 1th step update jason data: " + JSON.stringify(fileUploadArgs));
            var updateFileUrl = "https://" + window.location.host + "/api/v1/courses/" + stanford_syl_course_id + "/files" ;
            console.log("Upload file 1th step upload URL: " + JSON.stringify(fileUploadArgs));
            $.ajax({
              url: updateFileUrl,
              type: "POST",
              data: JSON.stringify(fileUploadArgs),
              contentType: "application/json",
              statusCode: {
                  200: function (response) {
                      console.log(JSON.stringify(response));
                      console.log("upload file upload_url: " + response.upload_url);
                      syl_uploadfile_mycomputer_upload(fileUploaded,response);
                      //location.reload();
                  }
             }
           });
        }


        function getCourseRootFolderID()
        {
            //https://stanford.test.instructure.com:443/api/v1/courses/$(course_id)/folders/by_path
            var location="https://" + window.location.host + "/api/v1/courses/" + stanford_syl_course_id + "/folders/by_path" ;
            var result = false;
            $.ajax({
                type: "get",
                data: "",
                url: location,
                //line added to get ajax response in sync
                async: false,
                success: function(data) {
                    result = data;
                },
                error: function() {
                    alert('Error occured');
                }
            });
            console.log("Upload file 1th step get course root folder return: " + JSON.stringify(result));
            return result;
        }


        function syl_uploadfile_mycomputer_upload(fileUploaded, uploadResponse)
        {
           var upload_url = uploadResponse.upload_url;
           console.log("Upload file 2th step upload_params: " + JSON.stringify(uploadResponse));

           var formData = new FormData();
           for (var key in uploadResponse.upload_params)
           {
               var val = uploadResponse.upload_params[key];
               formData.append(key, val);
           };
           formData.append("file",fileUploaded);

           $.ajax({
                url: upload_url,
                data: formData,
                type: "POST", //ADDED THIS LINE
                // THIS MUST BE DONE FOR FILE UPLOADING
                contentType: false,
                processData: false,
                /*
                statusCode: {
                  201: function (response) {
                      // DEBUG:
                      alert(JSON.stringify(response));
                      console.log(JSON.stringify(response));
                  }
                },*/
                success: function (response) {
                     //alert("---" +JSON.stringify(response));
                     console.log("Upload file 2th step return jason: " + JSON.stringify(response));
                     syl_uploadfile_mycomputer_upload_getURL(response);
                }
           });
        }


        function syl_uploadfile_mycomputer_upload_getURL(uploadResponse)
        {
           var location = uploadResponse.location;
           $.ajax({
                url: location,
                type: "GET",
                data: "",
                success: function (response) {
                     console.log("Upload file 3th step get upload file return jason: " + JSON.stringify(response));
                     syl_uploadfile_save_usuageRight(response.id);
                     syl_uploadfile_upload_to_syllabus(response);
                }
           });
        }


        $(document).on('change', '#stanford_syl_addfile_dialog_copyright_sel', function(){
            stanford_syl_selectedUsuageRight = $(this).find("option:selected").val();
            console.log("Upload file usuage right seletion: " + stanford_syl_selectedUsuageRight);
        });


        function syl_uploadfile_save_usuageRight(uploadCanvasFileID)
        {
            console.log("syl_uploadfile_save_usuageRight, user selectedUsuageRight: "+ stanford_syl_selectedUsuageRight);
            console.log("syl_uploadfile_save_usuageRight, fileID: " +uploadCanvasFileID);

            //Files - Set usage rights- PUT  /v1/courses/{course_id}/usage_rights
            var location = "https://" + window.location.host + "/api/v1/courses/" + stanford_syl_course_id +"/usage_rights";
            var dataStr = "file_ids[]=" + uploadCanvasFileID + "&publish=true&usage_rights[use_justification]=" + stanford_syl_selectedUsuageRight+"&_method=put";

            console.log("syl_uploadfile_save_usuageRight, update usuage right" + dataStr);
            //file_ids[]=4451050publish=trueusage_rights[use_justification]=own_copyright_method=put
            //data: "file_ids[]=4451050&publish=true&usage_rights[use_justification]=used_by_permission&_method=put",

            $.ajax({
                url: location,
                data: dataStr,
                type: "POST", //ADDED THIS LINE
                statusCode: {
                  200: function (response) {
                      // DEBUG:
                      //alert("200" + JSON.stringify(response));
                      console.log("syl_uploadfile_save_usuageRight,  200, return jason:" + JSON.stringify(response));
                  },
                  400: function (response) {
                      // DEBUG:
                      //alert("400" + JSON.stringify(response));
                      console.log("syl_uploadfile_save_usuageRight,  400, return jason:" + JSON.stringify(response));
                  },
                  404: function (response) {
                      // DEBUG:
                      //alert("404" + JSON.stringify(response));
                      console.log("syl_uploadfile_save_usuageRight,  404, return jason:" + JSON.stringify(response));
                  }
                }
           });
         }


        function syl_uploadfile_upload_to_syllabus(uploadResponse)
        {
            var fileJustUploaded = {
                fileName: uploadResponse.display_name,
                url: uploadResponse.url
            };

            syl_upload_to_syllabus(fileJustUploaded);
        }


        function getSyllabusBody()
        {
            //Course - GET https://canvas.stanford.edu:443/api/v1/courses/20973?include[]=syllabus_body
            var location="https://" + window.location.host + "/api/v1/courses/" + stanford_syl_course_id + "?include[]=syllabus_body" ;
            var result = "";
            $.ajax({
                type: "get",
                data: "",
                url: location,
                //line added to get ajax response in sync
                async: false,
                success: function(data) {
                    result = data;
                },
                error: function() {
                }
            });
            console.log("getSyllabusBody result json: " + JSON.stringify(result));
            return result;
        }

        function syl_upload_to_syllabus(fileJustAdded)
        {
            console.log("syl_upload_to_syllabus, jason pass to api call: "+ JSON.stringify(fileJustAdded));

            stanford_syl_uploaded_file = fileJustAdded;

            syl_uploadfile_upload_to_syllabus_1();


            var url =fileJustAdded.url.replace("download_frd", "wrap");
            var courseSyllabusInnerHTML ='<p><span class="instructure_file_holder link_holder"> \
                                             <a class="instructure_file_link" title="' + fileJustAdded.fileName + '" href="'+url+'"  \
                                                       data-mce-href="'+url+'">' + fileJustAdded.fileName + '</a> \
                                             <a class="file_preview_link" aria-hidden="true" href="'+url+'" title="Preview the document" \
                                                       style="padding-left: 5px;"><img src="/images/preview.png" alt="Preview the document"></a> \
                                          </span></p> ';

            window.parent.$('#course_syllabus').html(courseSyllabusInnerHTML);
            window.parent.$('#course_syllabus').append(syllabusTagInnerHTML);

            window.parent.$('#stanford_syl_add_file_div').css("display", "none");
            window.parent.$('#stanford_syl_edit_file_div').css("display", "none");
            window.parent.$('#stanford_syl_add_file_replace_div').css("display", "block");
            window.parent.$('#stanford_syl_edit_file_replace_div').css("display", "block");

            //window.parent.location.reload();
        }


        function syl_uploadfile_upload_to_syllabus_1()
        {
            var url =stanford_syl_uploaded_file.url.replace("download_frd", "wrap");
            var inertFile = '<p><a class="instructure_file_link instructure_scribd_file" title="' + stanford_syl_uploaded_file.fileName +  ' "href="'+url+ '" data-mce-href="'+url+ '">' + stanford_syl_uploaded_file.fileName+'</a></p>';

            var location = "https://" + window.location.host + "/api/v1/courses/" + stanford_syl_course_id ;
            $.ajax({
                url: location,
                //async: false,
                type: "PUT",
                data: { "course[syllabus_body]": inertFile },
                success: function (response) {
                    stanford_syl_syllabus_body = inertFile;
                }
            });
         }


         $(document).on('click', '#stanford_syl_add_file_btn', function()
         {
              loadSyllabusAddFileDialog();
             $(".stanford_syl_addfile_dialog").dialog('open');

             //diable Add button
             $("#stanford_syl_addfile_dialog_add").button("option", "disabled", true);

    	 });


        $(document).on('click', '#stanford_syl_add_file_replace_btn', function()
         {
            loadSyllabusAddFileDialog();

            $(".stanford_syl_addfile_dialog").dialog('open');
            $(".stanford_syl_addfile_dialog").dialog('option', 'title', 'Replace syllabus content');

            //diable Add button
            $("#stanford_syl_addfile_dialog_add").text("Replace");
            $("#stanford_syl_addfile_dialog_add").button("option", "disabled", true);

    	 });


      var syllabusFilwUploadInoutTag;
      function loadSyllabusAddFileDialog()
      {

           if(!$('body').find('#stanford_syl_addfile_dialog').size())
           {
                $("body").append('<div class="stanford_syl_addfile_dialog" id="stanford_syl_addfile_dialog" title="Add a file"> \
                                    <span>Select file from \
                                     <form id="stanford_syl_addfile_radio_form"> \
                                         <div> \
                                             <input type="radio" class="stanford_syl_addfile_radio" name="stanford_syl_addfile_radio" value="myComputer" checked="checked"> \
                                             <label>my computer&nbsp;&nbsp;&nbsp;&nbsp;</label> \
                                             <input type="radio" class="stanford_syl_addfile_radio" name="stanford_syl_addfile_radio" value="myCourseFiles"> \
                                            <label>my course\'s Files</label> \
                                         </div> \
                                    </form> </span>\
                                    <div id="stanford_syl_addfile_myconputer_div" style="display:block;"><span id="stanford_syl_addfile_myconputer_span" style="display:inline_block;"><form class="hidden"><input id="stanford_syl_addfile_mycomputer_upload" type="file" /></form><button id="stanford_syl_addfile_mycomputer_upload_btn" type="button">Choose file</button></span> \
                                         <span id="stanford_syl_addfile_myconputer_filename_span" style="display:inline_block;">&nbsp;&nbsp;No file chosen</span></div> \
                                 </div>');

                //$('body').append(syllabusAddFileDialogR); // This shows up the first click only.


                      $(".stanford_syl_addfile_dialog").dialog({
                          autoOpen: false,
                          resizable: false,
                          modal: true,
                          show: 'clip',
                          height: 'auto',
                          appendTo: "form",
                          width: 700,
                          buttons: [
                              {
                                  text: "Cancel",
                                  id: "stanford_syl_addfile_dialog_cancel",
                                  class: "Button",
                                  click: function()
                                  {
                                      clearDialog();
                                      $(this).dialog("close");
                                  }
                              },
                              {
                                  text: "Add",
                                  id: "stanford_syl_addfile_dialog_add",
                                  class: "Button Button--primary",
                                  click: function()
                                  {
                                      syl_uploadfile_mycomputer_add(stanford_upload_file);
                                      clearDialog();
                                      $(this).dialog("close");
                                  }
                              }
                          ]
                      });

                      syllabusFilwUploadInoutTag = document.getElementById("stanford_syl_addfile_mycomputer_upload");
                      syllabusFilwUploadInoutTag.addEventListener("change", syllabusFilwUploadInoutTagChange);
            }
            else
            {
                //alert("Opened already");
            }
        }


        //$(document).on('input','#stanford_syl_addfile_mycomputer_upload', function () {
        //$('#stanford_syl_addfile_mycomputer_upload').change(function() {
        function syllabusFilwUploadInoutTagChange(event)
        {
         $("#stanford_syl_addfile_dialog_add").button("option", "disabled", false);

         stanford_upload_file=$('#stanford_syl_addfile_mycomputer_upload')[0].files[0];
         console.log("uploaded File name: " + stanford_upload_file.name);
         var selectItem = $(this).find("option:selected").val();

         $(".stanford_syl_addfile_dialog #stanford_syl_addfile_myconputer_filename_span").html("&nbsp;&nbsp;"+stanford_upload_file.name+"&nbsp;&nbsp;");

         if (!$('#stanford_syl_addfile_dialog_copyright_sel').length)
         {
             $(".stanford_syl_addfile_dialog #stanford_syl_addfile_myconputer_filename_span").append(' \
                <select type="text" id="stanford_syl_addfile_dialog_copyright_sel" style=”display: inline-block;resize:both;”> \
                  <option value="">Choose usage rights...</option> \
                  <option value="own_copyright" selected="selected">I hold the copyright</option> \
                  <option value="used_by_permission">I have obtained permission to use this file.</option> \
                  <option value="public_domain">The material is in the public domain</option> \
                  <option value="fair_use">The material is subject to fair use exception</option> \
                  <option value="creative_commons">The material is licensed under Creative Commons</option>  \
               </select>         ');
         }
       }


        /*************************************************************************
     	 * End of CAN-242
     	 **************************************************************************/

	/***********************************
	 * CAN-155 - Add People Customization *
	 * Update for CAN-183
	 ***********************************/


	 function _nextButton(e) {
		 setTimeout(function () {

			 var src = e.target || e.srcElement;

			 if (src && src.id == 'addUsers' && src.getAttribute('title') == 'Add People') {
				 //alert ("clicked on " + src.id);
				 e.preventDefault();
				 var addpeople = document.getElementsByClassName('addpeople__peoplesearch');

				 if (addpeople) {

					 var span = addpeople[0].getElementsByTagName('span');
					 var legend = addpeople[0].getElementsByTagName('legend');
					 legend[0].style.display = 'none';

					 var email_radio_btn = document.getElementById("peoplesearch_radio_cc_path");
					 var font_class = email_radio_btn.nextSibling.childNodes[1].getAttribute("class");

					 var constom_span = document.createElement("span");
					 constom_span.setAttribute("id", "constom_span");
					 constom_span.classList.add(font_class);
                                         var para1 = document.createElement("p");
                                         var ptext1_1 = document.createTextNode("Add people by SUNet ID, separated by commas or line breaks. If the person you are adding doesn’t have a SUNet ID, please read the ");
                                         var atag = document.createElement("a");
                                         var linkText = document.createTextNode("guest account policy");
                                         atag.appendChild(linkText);
                                         atag.title = "guest account policy";
                                         atag.href = "https://canvashelp.stanford.edu/hc/en-us/articles/227082528-Stanford-Canvas-Guest-Accounts";
                                         para1.appendChild(ptext1_1);
                                         para1.appendChild(atag);
					 var ptext1_2 = document.createTextNode(".");
					 para1.appendChild(ptext1_2);

					 var para2 = document.createElement("p");
					 var btag = document.createElement("b");
					 var ptext2 = document.createTextNode("Add user(s) by");
					 btag.appendChild(ptext2);
					 para2.appendChild(btag);

					 constom_span.appendChild(para1);
					 constom_span.appendChild(para2);
                                         if (span.length > 0) {
					     span[2].appendChild(constom_span);
					     span[3].style.display = 'none';
                                         }


					 var fieldsets = addpeople[0].getElementsByTagName('fieldset');
					 if (fieldsets.length > 1) {
						 fieldsets[0].getElementsByTagName('label')[2].style.display = 'none';
						 document.getElementById('peoplesearch_radio_unique_id').parentNode.childNodes[1].childNodes[1].innerHTML = 'SUNet ID';
						 fieldsets[1].getElementsByTagName('div')[0].style.display = 'none';
					 }
				 }
				 $('.peoplesearch__instructions').hide();

				 var sunet_radio_btn = document.getElementById("peoplesearch_radio_unique_id");
				 var email_radio_btn_pn_pn = email_radio_btn.parentNode.parentNode;
				 var sunet_radio_btn_pn_pn = sunet_radio_btn.parentNode.parentNode;
				 email_radio_btn_pn_pn.parentNode.insertBefore(sunet_radio_btn_pn_pn, email_radio_btn_pn_pn.parentNode.firstChild);

				 sunet_radio_btn.click();
			 }

		 }, 100);
	 }

	 document.addEventListener('click', _nextButton);


/***********************************
 * end of Add People Customization *
 ***********************************/

/***********************************
 * Begin of CAN-243: Mark Grading Complete Customization *
 ***********************************/

   var ungraded_quizzes = [];
   var process_counter = 0;
   var course_id = 0;

   if (window.location.href.indexOf("gradebook") > -1){
   if (ENV.context_asset_string) {
    course_id = ENV.context_asset_string.split('_')[1];
   }
   // ONLY show pulldown for these courses.  Use course_id
   // Sp19-HUMBIO-4A-01: 98405 ,  Sp19-HUMBIO-4B-01 :98413
   if ((course_id == '98405') || (course_id == '98413') || (course_id == '100033') || (course_id == '78940') || (course_id == '86039') || (course_id == '104265') || (course_id == '104260')){
     //  show mark for grading complete button if at least one quiz contains ungraded questions.
     if ($("#gradebook_grid").length == 1) {

       // check if any quizzes are pending_review
       var all_quizzes = [];
       var get_all_quizzes_api = "https://" + window.location.host + "/api/v1/courses/" + course_id + "/quizzes?per_page=100";

       $.when(get_all_quizzes(get_all_quizzes_api,all_quizzes)).done(function(value) {
         //get_ungraded_quizzes(all_quizzes);
         $.when(get_ungraded_quizzes(all_quizzes)).done(function(value) {
           if (ungraded_quizzes.length > 0) {
             $("#keyboard-shortcuts").before('<span style="margin-top:10px; margin-right:5px">Mark Grading as Complete for </span> \
             <select style="margin-right:10px" id="ungraded_quizzes_select" > <option value=""  >Choose Assignment</option> </select>');
             $.each(ungraded_quizzes,function(index,value){
               $('#ungraded_quizzes_select').append($("<option></option>").attr("value", value.quiz_id).text(value.quiz_title));
             });

             $("#ungraded_quizzes_select").change(function() {
               quiz_id = $("#ungraded_quizzes_select option:selected").val();
               quiz_text = $("#ungraded_quizzes_select option:selected").text();
               mark_grading_complete(quiz_id, quiz_text);
             });
           }
         });
       });
     }
   }
 }




   function get_all_quizzes(get_all_quizzes_api, all_quizzes){
     var get_all_quizzes_deferred = $.Deferred();
     $.ajax({
       url: get_all_quizzes_api,
       type: "GET",
       data: "",
       statusCode: {
         200: function (response) {
           $.each(response, function (index, value) {
             var quiz_id = value.id;
             var quiz_title = value.title;
             var quiz_type = value.quiz_type;
             if (quiz_type == "assignment"){       // we only care about quizzes with quiz_type = assignment,which are graded quiz.
             var obj_quiz = {
               quiz_id: quiz_id,
               quiz_title: quiz_title
             };


             all_quizzes.push(obj_quiz); //  these are quizzes with due date. They should show up in Grades tool.
           }
           });
           get_all_quizzes_deferred.resolve("success");
         }
       }

     });

     return get_all_quizzes_deferred.promise();
   }


   function get_ungraded_quizzes(all_quizzes){
     var get_ungraded_quizzes_deferred = $.Deferred();
     var total_quiz_count = all_quizzes.length;

     $.each(all_quizzes, function (index, value) {
       var quiz_id = value.quiz_id;
       var quiz_title =value.quiz_title;
       var get_quiz_submissions_url = "https://" + window.location.host + "/api/v1/courses/" + course_id + "/quizzes/" + quiz_id + "/submissions?per_page=100";


       $.when(recursive_get_ungraded_quizzes(course_id, quiz_id,quiz_title, get_quiz_submissions_url, ungraded_quizzes)).done(function(value) {
         if (process_counter == total_quiz_count){
           get_ungraded_quizzes_deferred.resolve("find ungraded quizzes");
         }


       });

     });


     return get_ungraded_quizzes_deferred.promise();

   }

   function recursive_get_ungraded_quizzes(course_id, quiz_id, quiz_title, get_quiz_submissions_url,ungraded_quizzes){

     var recursive_get_ungraded_quizzes_deferred = $.Deferred();
     $.ajax({
       url: get_quiz_submissions_url,
       type: "GET",
       data: "",
       statusCode: {
         200: function (response, textStatus, jqXHR) {
           var found_pending = false;
           $.each(response.quiz_submissions, function (index, value) {
             var workflow_state = value.workflow_state;

             if (workflow_state == "pending_review"){
               var ungraded_quiz = {               //  these are questions we need to update, they are ungraded with score of 0
                 quiz_id: value.quiz_id,
                 quiz_title: quiz_title
               };

               ungraded_quizzes.push(ungraded_quiz);

               found_pending = true;
               return false;         // as soon as we find one ungraded submission, we can move on to the next quiz
             }

           });

           if (!found_pending) {
             // process the next page of 100

             var linkheader = jqXHR.getResponseHeader('Link');
             var nextlink = getNextLink(linkheader);
             if (nextlink !== null && nextlink.trim()!== ''){
               $.when(recursive_get_ungraded_quizzes(course_id, quiz_id,quiz_title, nextlink, ungraded_quizzes)).done(function(value) {
                 recursive_get_ungraded_quizzes_deferred.resolve("success"); // needed to resolve the outer $.when
               });
             }
             else {
               process_counter = process_counter + 1;
               recursive_get_ungraded_quizzes_deferred.resolve("success");
             }
           }
           else {
             process_counter = process_counter + 1;
             recursive_get_ungraded_quizzes_deferred.resolve("success");
           }

         }

       }

     });

     return recursive_get_ungraded_quizzes_deferred.promise();
   }


 // select one quiz only.
 function mark_grading_complete(quiz_id, quiz_text){
   var course_id = ENV.context_asset_string.split('_')[1];
   var NewDialog = $('<div class="popup_stanford_mark_grading_complete" title="Mark Assignment as Complete"> \
   <p>You have selected the following assignment to mark grading as complete: \
   <br/> - ' + quiz_text +
   '<br/> <br/> \
   <p>Clicking <strong>Proceed</strong> will convert all ungraded zero point questions within this assignment to graded. This will render grading complete and the assignment icon within the affected cells will be replaced with the assignment score. \
   <br/> <br/> \
   <strong>NOTE:</strong> This process could take a while depending on the size of your class. In some cases, you may need to select the assignment again if you still see the assignment icon for students.</p> \
   </div>');
   NewDialog.dialog({
     resizable: false,
     modal: true,
     show: 'clip',
     height: 'auto',
     width: 600,
     buttons: [
       {
         text: "Cancel",
         "class": 'Button',
         click: function() {
           $(this).dialog("close");  // Cancel code here
         }
       },
       {
         text: "Proceed",
         "class": 'Button Button--primary',
         click: function() {
           get_stats(course_id, quiz_id);
           $(this).dialog("close");
         }
       }
     ]
 });

 }

 function get_stats(course_id, quiz_id) {

   var get_stats_url = "https://" + window.location.host + "/api/v1/courses/" + course_id + "/quizzes/" + quiz_id + "/statistics?per_page=100";

   var ungraded_questions = [];
   $.ajax({
     url: get_stats_url,
     type: "GET",
     data: "",
     statusCode: {
       200: function (response) {
         $.each(response.quiz_statistics[0].question_statistics, function (index, value) {
           var questionid = value.id;
           if (value.question_type == 'essay_question' || value.question_type == 'file_upload_question'){
             $.each(value.answers, function (index, value) {
               var onequestion = {               //  these are questions we need to update, they are ungraded with score of 0
                 questionid: questionid,
                 user_names: value.user_names,
                 graded:value.id,
                 score: value.score,
                 attempt: 0
               };
               if (onequestion.graded == 'ungraded' && onequestion.score === 0){
                 ungraded_questions.push(onequestion);
               }

             });


           }
         });

         for (var i = 0; i < ungraded_questions.length; i ++ ){
           console.log(ungraded_questions[i]);
         }


         var quiz_submissions = [];
         setTimeout(function(){ get_quiz_submissions(course_id, quiz_id,ungraded_questions,quiz_submissions); }, Math.random() * 1000);
       }
     }
   });
 }

 function get_quiz_submissions(course_id, quiz_id,ungraded_questions,quiz_submissions) {
   // call submission api to get quiz_submission.
   //  https://stanford.instructure.com/api/v1/courses/14942/quizzes/57464/submissions
   var get_quiz_submissions_url = "https://" + window.location.host + "/api/v1/courses/" + course_id + "/quizzes/" + quiz_id + "/submissions?per_page=100";
   $.when(callQuizSubmissionAPI(course_id, quiz_id,ungraded_questions, get_quiz_submissions_url,quiz_submissions)).done(function(value) {
     update_scores(course_id, quiz_id,ungraded_questions,quiz_submissions);
   });
 }

 function callQuizSubmissionAPI(course_id, quiz_id,ungraded_questions, apiURL,quiz_submissions){

   var callQuizSubmissionAPI_deferred = $.Deferred();
   $.ajax({
     url: apiURL,
     type: "GET",
     data: "",
     statusCode: {
       200: function (response, textStatus, jqXHR) {

         $.each(response.quiz_submissions, function (index, value) {
           var quiz_submission_id = value.id;
           var workflow_state = value.workflow_state;
           if (workflow_state == "pending_review"){
           var one_submission = {               //  these are all submissions
             quiz_submission_id: quiz_submission_id,
             user_id: value.user_id,
             attempt:value.attempt,
             fudge_points:value.fudge_points
           };
           quiz_submissions.push(one_submission);
         }
         });
         var linkheader = jqXHR.getResponseHeader('Link');
         var nextlink = getNextLink(linkheader);
         if (nextlink !== null && nextlink.trim()!== ''){

           $.when(callQuizSubmissionAPI(course_id, quiz_id,ungraded_questions, nextlink,quiz_submissions)).done(function(value) {
             callQuizSubmissionAPI_deferred.resolve("success"); // needed to resolve the outer $.when
           });
 }
         else {
           callQuizSubmissionAPI_deferred.resolve("success");
         }
       }
     }
   });

   return callQuizSubmissionAPI_deferred.promise();
 }


 function getNextLink(linkheader){

   var result = null;
   var links = linkheader.split(',');
   for (var i = 0; i < links.length; i ++ ){
     {
       var linkPart = links[i].split(";");
       if (linkPart[1].indexOf("rel=\"next\"") > 0)
       {
         result = linkPart[0].trim();
         break;
       }
     }
   }

   if (result && !(0 === result.length))
   {
     if (result.startsWith("<"))
     {
       result = result.substring(1, result.length - 1);
     }
   }

   return result;
 }

 function update_scores(course_id, quiz_id,ungraded_questions,quiz_submissions) {

   var question_arr = "";
   for (var i = 0; i < ungraded_questions.length; i ++ ){
     question_arr += ("\""+ ungraded_questions[i].questionid + "\""+ ":{ \"score\": 0},");
   }

   question_arr =question_arr.substring(0, question_arr.length-1);

   for (var i = 0; i < quiz_submissions.length; i ++ ){
     var updateScoreUrl = "https://" + window.location.host + "/api/v1/courses/" + course_id + "/quizzes/" + quiz_id + "/submissions/" + quiz_submissions[i].quiz_submission_id;
     var payload = "{ \
       \"quiz_submissions\": [\
         {\
           \"attempt\": " + quiz_submissions[i].attempt + ",\
           \"fudge_points\": " + quiz_submissions[i].fudge_points + ",\
           \"questions\": {" + question_arr + "\
         }\
       }\
     ]\
   }";

   $.ajax({
     url: updateScoreUrl,
     type: "PUT",
     data: payload,
     contentType: "application/json",
     statusCode: {
       200: function (response) {
         location.reload();
       }
     }
   });
 }

 }
/***********************************
 * End of CAN-243: Mark Grading Complete Customization *
 ***********************************/
 
 /*******************************************************************************
  * CAN-283 Link to student mental health resources
  **********************************************************************/
  
 if (window.location.pathname == "/") {
   setTimeout(function() {

  if (window.location.pathname == "/") {
     if ($("h1.ic-Dashboard-header__title").length == 1) {
       
        var $wellnessInsertElement = `
       
        <div style="text-align:center; font-size:.85rem; background-color:#edd; border:2px solid #a44; border-radius:5px; padding-right:10px; padding-left:10px;">

          <p>

           <a href="http://wellbeing.stanford.edu">Well-being resources for students<br>
             
           <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="92" height="40" viewBox="0 0 92 40">
             <image width="92" height="40" xlink:href="data:img/png;base64,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"/>
           </svg>
          
          
             </a>

             </p>
      

           <p>

            <a href="http://redfolder.stanford.edu">Red folder resource for faculty/staff assisting distressed students<br>

            <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="40" width="40"
               viewBox="0 0 150 150" style="enable-background:new 0 0 144 116;" xml:space="preserve">
            <style type="text/css">
              .st0{fill-rule:evenodd;clip-rule:evenodd;fill:#721412;}
              .st1{fill-rule:evenodd;clip-rule:evenodd;fill:#8C191C;}
              .st2{fill:#FFFFFF;}
              .st3{fill:#8C191C;}
              .st4{fill:#A81D37;}
            </style>
            <g>
              <path class="st0" d="M58.6,14.7h63.5c6.3,0,10.9,5.1,10.9,10.9v15.1c0,0.4-0.4,0.8-0.8,0.8H11.9c-0.4,0-0.8-0.4-0.8-0.8V15.5
                c0-5.9,5.1-10.9,10.9-10.9h24.4C53.1,4.6,55.6,9.6,58.6,14.7z"/>
              <path class="st1" d="M9.4,43.2h125.3c5.5,0,9.7,5.5,8,10.9L128,102.5c-1.7,4.6-5.9,8-10.5,8H26.6c-4.6,0-8.8-3.4-10.5-8L1.4,54.1
                C-0.3,48.6,3.9,43.2,9.4,43.2z"/>
            </g>
            <g>
              <g>
                <path class="st2" d="M76.4,70.9c0.2,0.1,0.4,0.3,0.6,0.4c0,0,0,0,0,0h5.7l6.7,6.7v19l-7.7,7.4H61.5L53.8,97V86.9h10.2
                  c0,0,0-0.1,0-0.1c0-0.1,0.1-0.2,0.2-0.3H53.5v10.8l7.9,7.7h20.6l7.9-7.6V77.9L83,70.9H76.4z"/>
                <path class="st2" d="M81.9,50.3H61.4l-7.9,7.6v20.2l6.9,6.9h3.1c0-0.2,0-0.3,0.1-0.5h-3.1l-6.7-6.7V58.1l7.7-7.4h20.2l7.7,7.4
                  v11.1l-10.1,0c0,0.2,0,0.3,0,0.5h10.7V58L81.9,50.3z"/>
              </g>
              <polygon class="st2" points="69.6,83.7 60.8,83.7 54.7,77.6 54.7,58.5 61.8,51.6 81.3,51.6 88.4,58.5 88.4,68.3 72.9,68.3 
                72.9,72.2 82.3,72.2 88.4,78.4 88.4,96.6 81.3,103.5 61.8,103.5 54.7,96.6 54.7,87.8 64.8,87.8 69.6,87.8 	"/>
              <polygon class="st2" points="69.4,84.6 60.5,84.6 53.8,77.9 53.8,58.1 61.5,50.7 81.7,50.7 89.4,58.1 89.4,69.2 72.9,69.2 
                72.9,71.3 82.7,71.3 89.4,78 89.4,97 81.7,104.4 61.5,104.4 53.8,97 53.8,86.9 69.6,86.9 	"/>
              <g>
                <path class="st3" d="M74.3,78.5c0.3,0.3,1.8,1.3,2.3,1.5c1.1,0.5,1.7,1.4,2.1,2.4c0.3,1,0,0.8-0.3,0.7c-0.3-0.1-0.3-0.4-1-0.4
                  c-0.7,0-1.1,0-1.5-0.4c-0.1-0.1-0.2-0.2-0.3-0.3c0,0,0,0,0,0c-0.5-0.3-0.4,0.8-0.3,1c0.3,0.7,0.6,0.4,2.5,1.4
                  c0.9,0.5,1.1,1.1,1.2,1.4c0.2,0.4,0.3,0.6-1.1,0.4c-0.4-0.1-1.2-0.3-1.6-0.6c-0.4-0.2-1.1-0.1-1,0.5c0.3,0.8,1.2,1.3,2.1,1.4
                  c0.7,0.1,1.1,0.2,1.2,0.4c0.4,0.4-0.3,1.1-0.3,1.1c-0.4,0.4,0,0.9,0.3,1.1c0.4,0.2,1.3,0.7,1.6,1.5c1.5,3.8,0.1,2.7-0.7,2.3
                  s-2.1-1.6-3.3-1.5s-1.7,0.2-2.4-0.4c-0.7-0.6-0.7,0.4-0.7,0.4s0,1.1,0,4.6c0,1,0.2,2,1.1,2.8c0.7,0.7,1.2,0.6,2.2,1.7
                  c0.4,0.5,1.9,1.1,2.9,1.1H81l6.6-6.3V78.8l-5.6-5.6h-3.7c0.3,0.5,0.5,1.2,0.6,2.1c0,0.6-0.8,0.3-1,0.2c-0.2-0.1-0.4-0.2-0.7-0.3
                  c-0.6-0.1-1.9-0.7-2.3-0.8c-0.4-0.1-0.7,0.1-0.7,0.2l0,0c-0.1,0.2,0.1,0.5,0.1,0.5c0.5,1.2,1.5,1.1,2.6,1.9c1.5,1,0.7,1.2,0.4,1.1
                  s-0.8-0.1-0.8-0.1c-1.2,0.3-1.5-0.2-2.2-0.3C73.5,77.4,74.1,78.2,74.3,78.5z"/>
                <path class="st3" d="M67.7,100c0.5-0.7,1.3-1.3,1.8-1.8c0.5-0.5,0.6-1.8,0.7-3.1c0-2.1,0-2.8,0-2.8v0c0-0.3,0-0.5,0-0.7l0,0v-0.4
                  c0,0,0-0.1,0-0.1v-1.2c0-0.3-0.3-0.3-1,0.5c-0.7,0.8-1.9,0.7-2.6,0.8c-0.7,0.1-2.7,1.1-3.3,1.8c-0.4,0.5-0.9,0.1-0.7-0.8l0,0
                  c0.1-0.4,0.3-0.9,0.6-1.7c0.4-1,1.9-1.6,1.9-1.6s0.2-0.1,0.3-0.2H64l0,0h-8.4v7.5l6.6,6.3h2.1C66.3,102.5,67.1,101,67.7,100z"/>
                <path class="st3" d="M62.2,52.6l-6.6,6.3v18.3l5.6,5.6h5.3c0.9-0.4,1.1-0.3,1.3-0.8c0-0.1,0.1-0.3,0.1-0.5c0-0.1,0.1-0.7-0.2-0.6
                  c-0.6,0.3-1.7-0.4-2.6,0c-0.8,0.4-0.2-0.6-0.1-0.7c0,0,0.5-0.6,1.1-1c0,0,0.1,0,0.1,0c0.1,0,0.1-0.1,0.2-0.1
                  c0.5-0.2,2-1.2,2.3-1.5c0.2-0.2,0.4-0.6,0.5-0.8c0.1-0.2,0.1-0.5-0.1-0.6c-0.3-0.2-0.5,0.2-1,0.4s-0.8,0.3-1.2,0.3
                  c-0.4,0-0.7-0.1-1-0.1s-0.4-0.1,0.1-0.6c0.2-0.2,0.3-0.3,0.4-0.3c1-0.6,1.9-0.6,2.4-1.7c0,0,0.4-1-0.4-0.6
                  C68,73.7,67.8,74,66.6,74s-1.6,0.5-1.8,0.8c0,0-0.8,1.1-0.6-0.4c0.2-1.5,0.5-2.3,1.2-2.9c0.6-0.5,2.2-1.2,2.8-2
                  c0.3-0.3,1-1.1,0.6-1.8c-0.2-0.3-0.6,0.5-1.1,0.6l0,0c-0.5,0.1-1.2,0.3-1.7,0.2c-0.6-0.1-1,0.1-1.2,0.2s-0.7-0.2-0.1-0.8
                  c0.7-0.8,2.4-1.8,3.6-2.5c0.2-0.1,0.6-0.2,0.9-0.5c0,0,0,0,0,0c0.1,0,0.2-0.1,0.3-0.2c0.3-0.2,0.4-0.4,0.4-0.7
                  c-0.1-0.2-0.2-0.3-0.5-0.3c-0.3,0-0.7,0.3-1.1,0.2c-0.6-0.1-1.4,0.1-1.2-0.3c0.3-0.4,0.7-0.6,0.8-0.7c0.2-0.1,0.6-0.2,1-0.5
                  c0.7-0.3,0.6-1.2,0.3-1.2c-0.4-0.1-1.7,0.3-0.8-0.6c0,0,0.4-0.4,0.8-0.7c0.3-0.2,0.6-0.2,0.9-0.4c0.2-0.1,0.7-0.5-0.5-0.6
                  c0,0-0.7,0-0.6-0.3c0.1-0.2,0.7-0.6,0.7-0.6s0.5-0.3,0.7-0.5c0.2-0.2,0.3-0.3,0.3-0.5c0-0.2-0.5-0.4-0.7-0.7
                  c-0.2-0.2,0-0.2,0.1-0.3c0,0,0.1,0,0.2,0c0.5,0,0.6-0.5,0.9-1.8c0.1-0.4,0.1-0.5,0.2-0.5l0,0l0,0l0,0c0,0,0,0,0,0
                  c0,0,0.1,0.7,0.3,1.4c0.2,0.4,0.3,0.6,0.6,0.6c0.1,0,0.1,0,0.2,0c0.1,0,0.2,0.1,0.1,0.3c-0.1,0.1-0.4,0.4-0.5,0.5
                  c-0.1,0.4,0.3,0.5,0.7,0.6c0.6,0,0.3,0.4-0.3,0.8c-0.6,0.4,0.9,1.3,0.9,1.3c0.8,0.6,0.2,0.8,0.1,0.9c-0.2,0.1-0.7,0.4-0.2,0.6
                  c0.5,0.2,1.1,0.8,1.1,0.8c0.8,0.9-0.4,0.6-0.8,0.6c-0.3,0-0.4,0.9,0.3,1.2c1.1,0.5,1.4,0.6,1.8,0.9c0.7,0.5,0.3,1-0.6,0.8
                  c0,0-0.6-0.2-1-0.1c-0.3,0.1-0.4,0.1-0.6,0.2c-0.1,0.1-0.2,0.5,1.1,0.9c0.6,0.2,1.4,0.7,2.1,1.2l10.6,0v-8.5l-6.6-6.3L62.2,52.6
                  L62.2,52.6z"/>
                <path class="st4" d="M89.4,58.1l-7.7-7.4H61.5l-7.7,7.4v19.8l6.7,6.7h3.1c-0.1,0.2-0.2,0.5,0,0.8c0.2,0.3,0.6,0.3,0.8,0.3
                  c0.2,0,0.4,0,0.8-0.1l0,0c0,0,0.2,0.1-0.3,0.3l0,0c-0.4,0.1-0.8,0.4-0.9,0.8c0,0,0,0.1,0,0.1H53.8V97l7.7,7.4h20.2l7.7-7.4V78
                  l-6.7-6.7H77h0c-0.2-0.2-0.5-0.3-0.7-0.4l-0.1-0.1l0,0c-0.1-0.1-0.3-0.2-0.4-0.3c-0.1-0.1-0.2-0.2-0.3-0.3l0,0
                  c-0.2-0.2-0.3-0.3-0.4-0.4c0.9,0.2,1.8,0.3,2.3,0.3h0.1c0,0,0.1,0,0.1,0h0c0.1,0,0.2,0,0.2,0c0.1,0,0.1,0.1,0.2,0.1l0.2,0.1
                  c0.1,0,0.1,0,0.2,0c0.3,0,0.7-0.2,0.8-0.5c0.1-0.1,0.1-0.3,0.1-0.6l10.1,0L89.4,58.1L89.4,58.1z M88.4,68.3H77.9
                  c0.2,0.2,0.4,0.4,0.5,0.6c0.5,0.6,0.1,0.9-0.2,0.8c0,0-0.2-0.1-0.3-0.1c-0.1,0-0.6-0.1-0.6-0.1c-0.6,0-2.1-0.1-3-0.6
                  c-0.4-0.2-0.4,0.3-0.2,0.7c0.1,0.2,0.4,0.7,0.8,1.1c0.1,0.1,0.2,0.2,0.4,0.4c0.2,0.2,0.4,0.3,0.5,0.4l0,0c0.5,0.3,1,0.6,1.4,0.9h5
                  l6.2,6.1v18.2l-7.1,6.9H61.8l-7.1-6.9v-8.8h9.6l0,0h0.9c-0.1-0.1-0.3-0.3-0.5-0.4c0,0-0.8-0.7,1.1-0.9c0.8-0.1,1.7-0.6,2.1-1.4
                  c0.1-0.5-0.7-0.7-1-0.5c-0.4,0.2-1.2,0.5-1.6,0.6c-1.4,0.2-1.2,0.1-1.1-0.4c0.1-0.2,0.2-0.6,0.7-1h-4l-6.2-6.2V58.5l7.1-6.9h19.5
                  l7.1,6.9L88.4,68.3L88.4,68.3z"/>
              </g>
            </g>
            </svg>
            
          
              </a>
       
          `;
        
         $("#right-side").before($wellnessInsertElement);
     }
   };

   }, 1000);
 }
   
  /*******************************************************************************
   * End of CAN-283 Link to student mental health resources
   **********************************************************************/

   /*******************************************************************************
   * CAN-281 Make "Download Submissions" visible to only acct admins, not instructors
   **********************************************************************/
  
   if (window.location.href.indexOf("quizzes") > -1){
     
     setTimeout(function() {
  
       var canvasUserRoles = [ENV["current_user_roles"]];
       var courseId = ENV.context_asset_string.split('_')[1];
       var subAccount = null;
       var courseInfo = getCourseAccountByCourseId(courseId);
       subAccount = courseInfo.account_id;
       var isUserAnAdmin = false;
  
       // Disabling the download only applies to Law School Anonymous Grading subaccount 304

       if (courseId !== null) {
        if (subAccount === 304) {
       
         var stringOfRoles = canvasUserRoles.toString();
         var arrayOfRoles = stringOfRoles.split(",");
   
         arrayOfRoles.forEach(function (item, index) {
              if ((item === 'admin') || (item === 'root_admin')) {
                isUserAnAdmin = true;
              }
         });

         if (!isUserAnAdmin) {
             $('a#download_submission_button').remove();
         };
       };
      };

     }, 1000);
   
 }
  
   // Global function to retrieve account id passing courseid
  
  function getCourseAccountByCourseId(courseId)
  {
      //Course - GET https://canvas.stanford.edu:443/api/v1/courses/20973?include[]=syllabus_body
      var location="https://" + window.location.host + "/api/v1/courses/" + courseId;
      var result = "";
      $.ajax({
          type: "get",
          data: "",
          url: location,
          //line added to get ajax response in sync
          async: false,
          success: function(data) {
              result = data;
          },
          error: function() {
          }
      });
      console.log("getCourseAccountByCourseId result json: " + JSON.stringify(result));
      return result;
  }
  
  /*******************************************************************************
   * End of CAN-281 Make "Download Submissions" visible to only acct admins, not instructors
   *******************************************************************************/

   /*******************************************************************************
   * CAN-333 Provide warning about existing Gradebook going away Winter quarter
   **********************************************************************/
 
   if (window.location.href.indexOf("gradebook") > -1){
     
     var isUserNotStudent= false; 
     setTimeout(function() {
       
        var canvasUserRolesGradeBook = [ENV["current_user_roles"]];  
        var stringOfRolesGradeBook = canvasUserRolesGradeBook.toString();
        var arrayOfRolesGradeBook = stringOfRolesGradeBook.split(",");

        arrayOfRolesGradeBook.forEach(function (item, index) {
           // if user has any of these roles, dont consider the user as a student exclusively        
           if ((item === 'teacher') || (item === 'root_admin') || (item === 'admin') || (item === 'course_admin')) {
               isUserNotStudent = true;
             }
        });
        
        if (isUserNotStudent) {
          var breadCrumbMessage = $('.ic-app-crumbs');
          breadCrumbMessage.after('<div><p style="width: 610px; border:2px solid #a44; padding: 5px; font-size:.85rem; background-color:#edd;">A new Gradebook will replace the current one in Winter 2020. <strong><a href="https://canvashelp.stanford.edu/hc/en-us/articles/360034611074-New-Gradebook-Coming-in-Winter-2020"> Learn more, including how to try it now.</a></strong></p></div>');
        
        };
     
 
    }, 1000);
 
  }
 
  /*******************************************************************************
  * End of CAN-333 Provide warning about existing Gradebook going away Winter quarter
  **********************************************************************/
  

});
