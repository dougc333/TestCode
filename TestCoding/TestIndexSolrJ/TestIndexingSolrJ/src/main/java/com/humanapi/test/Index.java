package main.java.com.humanapi.test;


import org.apache.solr.client.solrj.SolrServerException;
import org.apache.solr.client.solrj.impl.HttpSolrServer;


public class Index {

	public static void main(String []args){
		try{
			HttpSolrServer server = new HttpSolrServer("http://hadoop.is-very-good.org:8983/solr/testme");
		    for(int i=0;i<1;++i) {
		      org.apache.solr.common.SolrInputDocument doc = new org.apache.solr.common.SolrInputDocument();
		      doc.addField("cat", "book");
		      doc.addField("id", "book-" + i);
		      doc.addField("name", "The Legend of the Hobbit part " + i);
		      server.add(doc);
		      server.commit();  // periodically flush
		    }
		    server.commit();
		}catch(Exception e){
			e.printStackTrace();
		}
		
		
	}
}
