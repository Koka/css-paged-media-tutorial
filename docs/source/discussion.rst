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

