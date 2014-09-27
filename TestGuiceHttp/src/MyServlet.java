

import java.io.IOException;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.google.inject.Singleton;

@Singleton
public class MyServlet extends HttpServlet{
	
	protected void doGet(HttpServletRequest request,HttpServletResponse response) throws IOException{
		System.out.println("doGet");
		response.setContentType("text/html");
        response.setStatus(HttpServletResponse.SC_OK);
		response.getWriter().println("<html><body>adsfas</body></html>");
	
	}
	protected void doPost( HttpServletRequest request,HttpServletResponse response) throws IOException{
		System.out.println("doPost");
		response.setContentType("text/html");
        response.setStatus(HttpServletResponse.SC_OK);
		response.getWriter().println("<html><body>adsfas</body></html>");
	}

}
