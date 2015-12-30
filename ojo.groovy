import groovy.swing.SwingBuilder
import java.awt.BorderLayout as BL

//@authored by Itamar Berman-Eshel
//A simple tool to check if a path in the oss-snapshot-local repository  on ojo exists and which properties it contains
//Run this by executing 'groovy ojo.groovy'
def swing = new SwingBuilder()
def panel = {
     swing.panel() {
        label("Please enter the desired path")
    }
}
swing.edt {

	//def user = "your user name (if needed)
	//def password = "your password (if needed)"
	def baseURL = "http://oss.jfrog.org/artifactory/api/storage/oss-snapshot-local/"

  frame(title: 'OJO path checker', size: [800, 200], show: true) {
    borderLayout()
    def input = textField(columns:10, actionPerformed: {}, constraints:BL.NORTH)
    def output = label(text: '', preferredSize: [100, 100], constraints: BL.SOUTH)
	  def checkPath = button(text:'Check Path', actionPerformed: {def path = "curl ${baseURL}${input.text}".execute().text; println path; output.text = "<html>Searching OJO for path: ${input.text}<br><br>${path}<html>"}, constraints:BL.WEST)
    def checkProps = button(text:'Check properties', actionPerformed: {def props = "curl ${baseURL}${input.text}?properties".execute().text; println props; output.text="<html>Searching OJO for properties on path: ${input.text}<br><br>${props}<html>"}, constraints:BL.EAST)
    widget(panel())
  }
  
}
