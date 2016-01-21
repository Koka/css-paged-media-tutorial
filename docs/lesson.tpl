Lesson: {{ name }}
=====================================================

.. include:: ../../{{ name }}/README.rst
 
 
.. raw:: html

   <link href="//cdn.rawgit.com/noelboss/featherlight/1.3.5/release/featherlight.min.css" type="text/css" rel="stylesheet" />
   <script src="//code.jquery.com/jquery-latest.js"></script>
   <script src="//cdn.rawgit.com/noelboss/featherlight/1.3.5/release/featherlight.min.js" type="text/javascript" charset="utf-8"></script>

Repository files
++++++++++++++++

- https://github.com/zopyx/css-paged-media-tutorial/tree/master/{{ name }}

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
            {% for entry in pdfs %}
                <tr>
                    <td>
                        {{ entry.name }}
                    </td>
                    <td>
                        {{ entry.status }}
                    </td>
                    <td>
                        <a href="_static/{{ name }}/{{ entry['pdf_file'] }}">Download</a>
                    </td>
                    <td>
                          {% for image in entry.images %} 
                            <a href="#" data-featherlight="_static/{{ name }}/images/{{ entry.name.lower() }}/{{ image }}" >
                                <img class="preview" src="_static/{{ name }}/images/{{ entry.name.lower() }}/thumb-{{ image }}" />
                            </a>
                          {% endfor %}
                    </td>
                    <td>
                          {% if entry.message %} 
                          {{ entry.message }}
                          {% endif %}
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>


{% if has_css %}
Stylesheet
++++++++++

.. literalinclude:: ../../{{ name }}/styles.css
  :language: css
  :linenos:

{% endif %}

{% if mode == 'html' %}
HTML input
++++++++++
.. literalinclude:: ../../{{ name }}/index.html
  :language: html
  :linenos:

{% endif %}

{% if mode == 'xml' %}
XML input
+++++++++
.. literalinclude:: ../../{{ name }}/index.xml
  :language: xml
  :linenos:

{% endif %}
