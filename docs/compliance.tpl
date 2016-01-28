<table border="0" class="table docutils">
    <thead>
        <tr>
            <th>Lesson</th>
            <th>PDFreactor</th>
            <th>PrinceXML</th>
            <th>Antennahouse</th>
            <th>Vivliostyle</th>
        </tr>
    </thead>
    <tbody>
        {% for lesson in rows %}
            <tr>
                <td>
                    <a href="{{ lesson}}.html">{{ lesson }}</a>
                    {% if rows[lesson]['readme'] %}
                        <div class="readme">
                            {{ rows[lesson]['readme'] }}
                        </div>
                    {% endif %}
                </td>
                <td>
                    {% if rows[lesson]['converters'].get('PDFreactor') %}
                        {{ rows[lesson]['converters']['PDFreactor']['status'] }}
                    {% endif %}
                </td>
                <td>
                    {% if rows[lesson]['converters'].get('PrinceXML') %}
                        {{ rows[lesson]['converters']['PrinceXML']['status'] }}
                    {% endif %}
                </td>
                <td>
                    {% if rows[lesson]['converters'].get('Antennahouse') %}
                        {{ rows[lesson]['converters']['Antennahouse']['status'] }}
                    {% endif %}
                </td>
                <td>
                    {% if rows[lesson]['converters'].get('Vivliostyle') %}
                        {{ rows[lesson]['converters']['Vivliostyle']['status'] }}
                    {% endif %}
                </td>
            </tr>
        {% endfor %}
    </tbody>
</table>
