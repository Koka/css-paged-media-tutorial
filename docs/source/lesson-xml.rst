Lesson: lesson-xml
=====================================================

.. include:: ../../lesson-xml/README.rst
 
 
.. raw:: html

   <link href="//cdn.rawgit.com/noelboss/featherlight/1.3.5/release/featherlight.min.css" type="text/css" rel="stylesheet" />
   <script src="//cdn.rawgit.com/noelboss/featherlight/1.3.5/release/featherlight.min.js" type="text/javascript" charset="utf-8"></script>

Repository files
++++++++++++++++

- https://github.com/zopyx/css-paged-media-tutorial/tree/master/lesson-xml

PDF files
+++++++++

 .. raw:: html

    <table class="table">
        <thead>
            <tr>
                <th>Converter</th>
                <th>Status</th>
                <th>PDF</th>
                <th>Images</th>
                <th>Comment</th>
            </tr>
        </thead>
        <tbody>
            
                <tr>
                    <td>
                        PDFreactor
                    </td>
                    <td>
                        OK
                    </td>
                    <td>
                        <a href="_static/lesson-xml/pdfreactor.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-xml/images/pdfreactor/pdfreactor.png" >
                                <img class="preview" src="_static/lesson-xml/images/pdfreactor/thumb-pdfreactor.png" />
                            </a>
                          
                    </td>
                    <td>
                          
                    </td>
                </tr>
            
                <tr>
                    <td>
                        PrinceXML
                    </td>
                    <td>
                        OK
                    </td>
                    <td>
                        <a href="_static/lesson-xml/prince.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-xml/images/princexml/prince.png" >
                                <img class="preview" src="_static/lesson-xml/images/princexml/thumb-prince.png" />
                            </a>
                          
                    </td>
                    <td>
                          
                    </td>
                </tr>
            
                <tr>
                    <td>
                        Antennahouse
                    </td>
                    <td>
                        undecided
                    </td>
                    <td>
                        <a href="_static/lesson-xml/antennahouse.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-xml/images/antennahouse/antennahouse.png" >
                                <img class="preview" src="_static/lesson-xml/images/antennahouse/thumb-antennahouse.png" />
                            </a>
                          
                    </td>
                    <td>
                           
                          does not render properly, eventually a configuration issue
                          
                    </td>
                </tr>
            
                <tr>
                    <td>
                        Vivliostyle
                    </td>
                    <td>
                        ERROR
                    </td>
                    <td>
                        <a href="_static/lesson-xml/vivliostyle-output.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-xml/images/vivliostyle/vivliostyle.png" >
                                <img class="preview" src="_static/lesson-xml/images/vivliostyle/thumb-vivliostyle.png" />
                            </a>
                          
                    </td>
                    <td>
                           
                          does not render properly, eventually a configuration issue
                          
                    </td>
                </tr>
            
        </tbody>
    </table>



Stylesheet
++++++++++

.. literalinclude:: ../../lesson-xml/styles.css
  :language: css
  :linenos:






XML input
+++++++++
.. literalinclude:: ../../lesson-xml/index.xml
  :language: xml
  :linenos:



.. raw:: html

    <hr/>

    <div id="disqus_thread"></div>
    <script>
    /**
    * RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
    * LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables
    */
    /*
    var disqus_config = function () {
        this.page.url = PAGE_URL; // Replace PAGE_URL with your page's canonical URL variable
        this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    */
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');

    s.src = '//printcssrocks.disqus.com/embed.js';

    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>