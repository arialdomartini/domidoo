<%namespace name="master" file="master.mak"/>
## calls the layout def
<%master:layout>
    <%def name="title()">Hello world!</%def>
    <%def name="header()">
        I am the header
    </%def>
    <%def name="sidebar()">
        <ul>
            <li>sidebar 1</li>
            <li>sidebar 2</li>
        </ul>
    </%def>

        this is the body
</%master:layout>
