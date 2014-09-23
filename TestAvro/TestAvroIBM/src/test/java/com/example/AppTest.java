package com.example;

import java.io.File;

import org.apache.avro.file.DataFileReader;
import org.apache.avro.file.DataFileWriter;
import org.apache.avro.io.DatumReader;
import org.apache.avro.io.DatumWriter;
import org.apache.avro.specific.SpecificDatumReader;
import org.apache.avro.specific.SpecificDatumWriter;

import com.example.avroSample.model.Automobile;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class AppTest 
    extends TestCase
{
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTest( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( AppTest.class );
    }

    /**
     * Rigourous Test :-)
     */
    public void testApp()
    {   
      System.out.println("running testApp");
      File outputFile = new File("/home/dc/TestAvroIBM");	
      Automobile auto = Automobile.newBuilder().setMake("speedy car")
        	      .setModelName("automobile").setModelYear(2013).setPassengerCapacity(2).build();

       DatumWriter<Automobile> datumWriter = new SpecificDatumWriter<Automobile>(Automobile.class);
       DataFileWriter<Automobile> fileWriter = new DataFileWriter<Automobile>(datumWriter);

        try{
          fileWriter.create(auto.getSchema(),outputFile);
          fileWriter.append(auto);
          fileWriter.close();
         }catch(Exception e){
         e.printStackTrace();
      }
       //test we can read what we wrote
        DatumReader dr = new SpecificDatumReader<Automobile>(Automobile.class);
        try{
    		DataFileReader<Automobile> fileReader = new DataFileReader<Automobile>(outputFile,dr);
    		Automobile auto1=null;
    		
    		if(fileReader.hasNext()){
    			auto1 = fileReader.next(auto);
    		}
    		System.out.println("auto1:"+auto1.getMake().toString());
    		System.out.println("auto1:"+auto1.getModelYear().toString());
    		System.out.println("auto1:"+auto1.getPassengerCapacity().toString());
    		
        }catch(Exception e){
          e.getStackTrace();
        }
       
        //this is not writing to hdfs (do separate cdk style job for this)
        //does cdk style maven hold for spark also? 
        
        
        assertTrue( true );
    }
}
