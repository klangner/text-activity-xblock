'''
Created on 08-09-2013

@author: Krzysztof Langner
'''
from pkg_resources import resource_string #@UnresolvedImport
from xblock.core import XBlock, Scope
from xblock.fields import String
from xblock.fragment import Fragment


class TextActivityBlock(XBlock):
    """
    An XBlock providing puzzle activity based on given image
    """

    text = String(help="Text with interactive elements", 
                      default="Sample \gap{Gap text} gap and \choice{option1 | option 2 | option 3}", 
                      scope=Scope.content)
    
    def student_view(self, context):
        html_str = resource_string(__name__, "static/textactivity/view.html")
        frag = Fragment(unicode(html_str).format(text=self.text))
        frag.add_css(unicode(resource_string(__name__, "static/textactivity/default.css")))       
        frag.add_javascript_url('http://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.1/underscore-min.js') 
        frag.add_javascript(unicode(resource_string(__name__, "static/textactivity/activity.js")))
        frag.initialize_js('TextActivityBlock')        
        return frag   
    
    @XBlock.json_handler
    def check(self, data):
        score = 0
        errors = []
        return {'score': score, 'errors': errors}    
    
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench.
                      <text>Sample \gap{Gap text} gap and \choice{option1 | option 2 | option 3}</text>
        """
        return [
            ("Text activity demo",
            """\
                <vertical>
                    <textActivity>
                    </textActivity>
                </vertical>
             """)
        ]