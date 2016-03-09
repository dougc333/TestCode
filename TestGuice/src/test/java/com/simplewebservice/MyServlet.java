package com.simplewebservice;

import java.io.IOException;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.google.inject.Singleton;

@Singleton
public class MyServlet extends HttpServlet{
	
	protected void doGet(HttpServletRequest request,HttpServletResponse response ) throws IOException{
		response.getWriter().println("asdfasdfsdfsad");
	}
}
