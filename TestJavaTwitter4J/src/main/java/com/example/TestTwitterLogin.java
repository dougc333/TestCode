package com.example;

import twitter4j.StallWarning;
import twitter4j.Status;
import twitter4j.StatusDeletionNotice;
import twitter4j.StatusListener;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;
import twitter4j.TwitterStream;
import twitter4j.TwitterStreamFactory;
import twitter4j.auth.Authorization;
import twitter4j.conf.Configuration;
import twitter4j.conf.ConfigurationBuilder;

public class TestTwitterLogin {
	public static void main(String []args) throws IllegalStateException, TwitterException{
	   System.setProperty("twitter4j.oauth.consumerKey", "eFIaiOuxsny01VVQ2QWISK1Mw");
       System.setProperty("twitter4j.oauth.consumerSecret", "gDQI5EiCMJJaaNI8XVNhfZXwuCOYfeJ3XsOUNHvsXqgq0Hoj9T");
       System.setProperty("twitter4j.oauth.accessToken", "76976448-Otz8w4yMKx6yCEWTH3dNTfuF8LYeLgqdoDrcl0oBK");
       System.setProperty("twitter4j.oauth.accessTokenSecret", "NFPFe2EzuKWuzRKmY1RENUBfQzGeGbAS1JzjX3Eu3GwDE");

	   TwitterStream twitterStream = new TwitterStreamFactory().getInstance();
       StatusListener listener = new StatusListener() {
           @Override
           public void onStatus(Status status) {
        	   System.out.println("----------STATUS---------");
               System.out.println("@" + status.getUser().getScreenName() + " - " + status.getText());               
           }

           @Override
           public void onDeletionNotice(StatusDeletionNotice statusDeletionNotice) {
        	   System.out.println("----------ONDELETIONNOTICE---------");
               System.out.println("Got a status deletion notice id:" + statusDeletionNotice.getStatusId());
           }

           @Override
           public void onTrackLimitationNotice(int numberOfLimitedStatuses) {
        	   System.out.println("----------LIMITATION---------");
               System.out.println("Got track limitation notice:" + numberOfLimitedStatuses);
           }

           @Override
           public void onScrubGeo(long userId, long upToStatusId) {
               System.out.println("Got scrub_geo event userId:" + userId + " upToStatusId:" + upToStatusId);
           }

           public void onStallWarning(StallWarning warning) {
               System.out.println("Got stall warning:" + warning);
           }

           @Override
           public void onException(Exception ex) {
               ex.printStackTrace();
           }
       };
       twitterStream.addListener(listener);
       twitterStream.sample();
	}
}
