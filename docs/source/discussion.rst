Discussion
==========


MathML support
--------------

Brought to the point: MathML support in all renderers is broken at the moment.
Lots of formatting and layout issues with native renderers and renderers based
on MathJax (Vivliostyle). It is questionable if MathML will ever work. The only
future for MathML is a cross-plattform support for a Javascript based rendering
engine like MathJax. However neither PrinceXML nor PDFreactor nor Antennahouse
support MathJax. So the only recommendation for using MathML directly: forget it.
The only valid option is to convert MathML somehow to LaTeX and then SVG. MathML
parts of your input should be replaced with a related SVG. However the toolchain
here also is not straight forward here.

Missing features and major pain
-------------------------------

- support for sidenotes (Antennahouse has its own extension)
- shapes and exclusions (there is a W3C CSS draft for shapes and exclusions)
- more flexible support for flots (every converter is dealing with floats differently
  and has its own extensions (Antennahouse in particular))
- working Javascript support. Working with Javascript in PrinceXML or PDFreactor is
  often a bit like gambling because you don't know which Javascript module is working
  with with processor. 
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
