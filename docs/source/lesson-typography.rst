Lesson: lesson-typography
=====================================================

.. include:: ../../lesson-typography/README.rst
 
 
.. raw:: html

   <link href="//cdn.rawgit.com/noelboss/featherlight/1.3.5/release/featherlight.min.css" type="text/css" rel="stylesheet" />
   <script src="//code.jquery.com/jquery-latest.js"></script>
   <script src="//cdn.rawgit.com/noelboss/featherlight/1.3.5/release/featherlight.min.js" type="text/javascript" charset="utf-8"></script>

Repository files
++++++++++++++++

- https://github.com/zopyx/css-paged-media-tutorial/tree/master/lesson-typography

PDF files
+++++++++

 .. raw:: html

    <table class="table docutils">
        <thead>
            <tr>
                <th>Converter</th>
                <th>PDF Preview</th>
            </tr>
        </thead>
        <tbody>
            
                <tr>
                    <td>
                        <span class="converter-name">PDFreactor</span>
                        <br/>
                        <span class="converter-status">ERROR</span>
                        <br/>
                        <a class="pdf-download" href="_static/lesson-typography/pdfreactor.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-typography/images/pdfreactor/pdfreactor.png" >
                                <img class="preview" src="_static/lesson-typography/images/pdfreactor/thumb-pdfreactor.png" />
                            </a>
                          
                           
                              <div>
                                no support for :first-line
                              </div>
                         
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <span class="converter-name">PrinceXML</span>
                        <br/>
                        <span class="converter-status">OK</span>
                        <br/>
                        <a class="pdf-download" href="_static/lesson-typography/prince.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-typography/images/princexml/prince.png" >
                                <img class="preview" src="_static/lesson-typography/images/princexml/thumb-prince.png" />
                            </a>
                          
                          
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <span class="converter-name">Antennahouse</span>
                        <br/>
                        <span class="converter-status">OK</span>
                        <br/>
                        <a class="pdf-download" href="_static/lesson-typography/antennahouse.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-typography/images/antennahouse/antennahouse.png" >
                                <img class="preview" src="_static/lesson-typography/images/antennahouse/thumb-antennahouse.png" />
                            </a>
                          
                          
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <span class="converter-name">Vivliostyle</span>
                        <br/>
                        <span class="converter-status">OK</span>
                        <br/>
                        <a class="pdf-download" href="_static/lesson-typography/vivliostyle-output.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-typography/images/vivliostyle/vivliostyle-0.png" >
                                <img class="preview" src="_static/lesson-typography/images/vivliostyle/thumb-vivliostyle-0.png" />
                            </a>
                           
                            <a href="#" data-featherlight="_static/lesson-typography/images/vivliostyle/vivliostyle-1.png" >
                                <img class="preview" src="_static/lesson-typography/images/vivliostyle/thumb-vivliostyle-1.png" />
                            </a>
                          
                          
                    </td>
                </tr>
            
        </tbody>
    </table>



Stylesheet
++++++++++

.. literalinclude:: ../../lesson-typography/styles.css
  :language: css
  :linenos:




HTML input
++++++++++
.. literalinclude:: ../../lesson-typography/index.html
  :language: html
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