

import java.util.EnumSet;

import javax.servlet.DispatcherType;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.DefaultServlet;
import org.eclipse.jetty.servlet.ServletContextHandler;

import com.google.inject.Guice;
import com.google.inject.servlet.GuiceFilter;

public class MyMain {

	
	public static void main(String []args) throws Exception{
		Guice.createInjector(new MyServletModule());
		Server server = new Server(8080);
		ServletContextHandler handler = new ServletContextHandler(server,"/",ServletContextHandler.SESSIONS);
		handler.addFilter(GuiceFilter.class,"/*",null);
		handler.addServlet(DefaultServlet.class,"/");
		server.start();
		server.join();
	}
	
}
