/*

write to stdout
adapt to the environment (SERVER_PORT)
make a system call
print out text/plain
parse apg output into <ul>
print out the template
==done==
use malloc for template and body
multi-line string literals?

*/

#include <stdio.h>
#include <stdlib.h>


int append(char a[], int i, char *s) {
    // Given an array, an index into that array, and a string, copy the string
    // to the given location in the array. Return the new index.
    int j;
    for (j=0; j < strlen(s); i++, j++) {
        a[i] = s[j];
    }
    return i;
}


int main() {

    // Variables
    // =========
    // These are used a couple times.

    char c;     // single character
    FILE *fp;   // file pointer


    // Read in the template.
    // =====================
    // Convert the entire file to a string (i.e., char array).

    char PAGE[1024 * 50]; // for now max template size is 50KB :)

    fp = fopen("template.html", "r");
    fread(PAGE, 1, sizeof(PAGE), fp);
    fclose(fp);


    // Branch based on port.
    // =====================

    char *head;
    char *body;
    char *port = getenv("SERVER_PORT");

    if (port == NULL) {
        // should return 400; requires whatever Apache setting so we
        // can write status line from CGI.
        head = "";
        body = "<p>Sorry, program! No port given!</p>\r\n";
    } else if (strcmp(port, "443") != 0) {
        // should redirect to https; here we don't absolutely have to have
        // access to the status line, because we can use an HTML redirect
        // (<meta http-equiv="refresh" />)
        head = "<meta http-equiv=\"refresh\" content=\"5; https://www.zetadev.com/passwords/\" />\r\n";
        body = "<p>The Easy Password Generator is only available over <a href=\"https://www.zetadev.com/passwords/\">an encrypted connection</a> (redirecting presently ...).</p>\r\n";
    } else {
        // proceed

        head = "";

        int i;
        char abody[197]; // (7 passwords * (10 char max + 9-char <li></li>) = 133
                         // + 9-char <ul></ul> = 142
                         // + 55-char "more..." link = 197

        fp = popen("apg -a0 -n7 -m8 -x10 -Mncl", "r");

        i = 0;
        i = append(abody, i, "<ul>");
        while ((c = getc(fp)) != EOF) {
            i = append(abody, i, "<li>");
            abody[i] = c, i++;
            while ((c = getc(fp)) != '\n') {
                abody[i] = c, i++;
            }
            i = append(abody, i, "</li>");
        }
        pclose(fp);

        i = append(abody, i, "<li><a href=\"/passwords/\">more ...</a></li>");
        i = append(abody, i, "</ul>");
        abody[i] = '\0';
        body = &abody[0];
    }


    // Output the HTML.
    // ================

    printf("Content-Type: text/html\r\n");
    printf("Pragma: no-cache\r\n");
    printf("Cache-Control: no-store, no-cache\r\n");
    printf("Expires: Fri, 30 Oct 1998 14:19:41 GMT\r\n");
        // http://www.mnot.net/cache_docs/#EXPIRES
    printf("\r\n");

    printf(PAGE, head, body, "C");
    printf("\r\n");

}
