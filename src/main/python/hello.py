import os, csv

def turn_Reference_Into_HTML_paragraph(file):
    general_path = "C:\\Users\\drew.hagen\\Desktop\\xsl called from\\out"
    i = 0
    with open(file, 'rb') as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            specific_path = general_path + str(i) + ".txt"
            print "\n<h3><a class=\"btn-primary plus\" onclick=\"myFunction('div"+str(i)+"')\">"+row[0]+"</a></h3>\n"
            if os.path.isfile(specific_path):
                with open(specific_path, 'rb') as infile:
                    line = infile.read()
                    s = ""
                    s += "<div id= \"div"+str(i)+"\" style=\"display: none;\"><table class=\"table table-bordered\">\n"
                    s += "\n\t<tr>\n\t\t<th>Called From File</th>\n\t\t<th>At Line</th>\n\t\t<th>Code Gist</th>\n\t</tr>\n"
                    lines = line.split("../../workspace/campus/")[2:]
                    if lines:
                        for l in lines:
                            s += "<p>" + split_into_html_table(switch_to_literal(l)) +\
                                  "</p>\n"
                        print s + "</table></div>"
                    else:
                        print "<div id= \"div"+str(i)+"\" style=\"display: none;\"><p>NONE</p></div>"
            i = i + 1


def switch_to_literal(html):
#if '&' in html:
    html = html.replace('&', "&amp;")
#if '<' in html:
    html = html.replace('<', "&lt;")
#if '>' in html:
    html = html.replace('>', "&gt;")
    return html

def split_into_html_table(plain_text):
    pieces = plain_text.split(':', 2)
    html = "\n\t<tr>"
    for piece in pieces:
        html += "\n\t\t<td>" + piece + "</td>"
    html += "\n\t</tr>"
    return html
