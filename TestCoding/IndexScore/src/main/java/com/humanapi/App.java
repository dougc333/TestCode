package com.humanapi;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
	SolrClient client = new HttpSolrClient("http://my-solr-server:8983/solr/core1");
   	QueryResponse resp = client.query(new SolrQuery("*:*"));

    }
}
