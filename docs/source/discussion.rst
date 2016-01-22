Discussion
==========

Missing features and major pain
-------------------------------

- support for sidde notes (Antennahouse has its own extension)
- shapes and exclusions (there is a W3C CSS draft for shapes and exclusions)
- more flexible support for flots (every converter is dealing with floats differently
  and has its own extensions (Antennahouse in particular))
- working Javascript support. Working with Javascript in PrinceXML or PDFreactor is
  often a bit like gambling because you don't know which Javascript module is working
  with with processor. 
- MathML support in a reasonable quality. All MathML renderers suck in their
  own special way. Being able to run MathJax (which has a very good quality)
  would solve much of the MathML pain.
- general support for adaptive image layout (doable with Javascript in PDFreactor)
- better control over the rendering process (e.g. through a Javascript API)
- better control over pagination (the page-break-* properties are kind of a
  joke since often the renderer do what they want)

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
