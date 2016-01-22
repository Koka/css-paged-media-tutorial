Lesson: lesson-page-numbers
=====================================================

.. include:: ../../lesson-page-numbers/README.rst
 
 
.. raw:: html

   <link href="//cdn.rawgit.com/noelboss/featherlight/1.3.5/release/featherlight.min.css" type="text/css" rel="stylesheet" />
   <script src="//cdn.rawgit.com/noelboss/featherlight/1.3.5/release/featherlight.min.js" type="text/javascript" charset="utf-8"></script>

Repository files
++++++++++++++++

- https://github.com/zopyx/css-paged-media-tutorial/tree/master/lesson-page-numbers

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
                        <a href="_static/lesson-page-numbers/pdfreactor.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-page-numbers/images/pdfreactor/pdfreactor-0.png" >
                                <img class="preview" src="_static/lesson-page-numbers/images/pdfreactor/thumb-pdfreactor-0.png" />
                            </a>
                           
                            <a href="#" data-featherlight="_static/lesson-page-numbers/images/pdfreactor/pdfreactor-1.png" >
                                <img class="preview" src="_static/lesson-page-numbers/images/pdfreactor/thumb-pdfreactor-1.png" />
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
                        <a href="_static/lesson-page-numbers/prince.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-page-numbers/images/princexml/prince-0.png" >
                                <img class="preview" src="_static/lesson-page-numbers/images/princexml/thumb-prince-0.png" />
                            </a>
                           
                            <a href="#" data-featherlight="_static/lesson-page-numbers/images/princexml/prince-1.png" >
                                <img class="preview" src="_static/lesson-page-numbers/images/princexml/thumb-prince-1.png" />
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
                        OK
                    </td>
                    <td>
                        <a href="_static/lesson-page-numbers/antennahouse.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-page-numbers/images/antennahouse/antennahouse-0.png" >
                                <img class="preview" src="_static/lesson-page-numbers/images/antennahouse/thumb-antennahouse-0.png" />
                            </a>
                           
                            <a href="#" data-featherlight="_static/lesson-page-numbers/images/antennahouse/antennahouse-1.png" >
                                <img class="preview" src="_static/lesson-page-numbers/images/antennahouse/thumb-antennahouse-1.png" />
                            </a>
                          
                    </td>
                    <td>
                          
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
                        <a href="_static/lesson-page-numbers/vivliostyle-output.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-page-numbers/images/vivliostyle/vivliostyle-0.png" >
                                <img class="preview" src="_static/lesson-page-numbers/images/vivliostyle/thumb-vivliostyle-0.png" />
                            </a>
                           
                            <a href="#" data-featherlight="_static/lesson-page-numbers/images/vivliostyle/vivliostyle-1.png" >
                                <img class="preview" src="_static/lesson-page-numbers/images/vivliostyle/thumb-vivliostyle-1.png" />
                            </a>
                          
                    </td>
                    <td>
                           
                          does not render the total amount of pages properly
                          
                    </td>
                </tr>
            
        </tbody>
    </table>



Stylesheet
++++++++++

.. literalinclude:: ../../lesson-page-numbers/styles.css
  :language: css
  :linenos:




HTML input
++++++++++
.. literalinclude:: ../../lesson-page-numbers/index.html
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