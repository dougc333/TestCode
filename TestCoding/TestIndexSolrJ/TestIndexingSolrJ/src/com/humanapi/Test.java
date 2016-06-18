package com.humanapi;

public class Test {

	public static void main(String []args){
		try{
			
			SolrClient client = new HttpSolrClient("http://my-solr-server:8983/solr/core1");
			QueryResponse resp = client.query(new SolrQuery("*:*"));

			
		}catch(Exception e){
			e.printStackTrace();
		}
		
	}
}
