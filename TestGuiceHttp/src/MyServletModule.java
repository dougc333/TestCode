

import com.google.inject.Binder;
import com.google.inject.Module;
import com.google.inject.servlet.ServletModule;

public class MyServletModule extends ServletModule{
	@Override
	protected void configureServlets(){
		serve("/*").with(MyServlet.class);
	}


}
