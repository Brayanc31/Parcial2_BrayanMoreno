%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int yylex(void);
void yyerror(const char *s);
%}

%token TRUE FALSE
%token AND OR NOT
%token NL

%left OR
%left AND
%right NOT

%%

input   : /* vacío */
        | input line
        ;

line    : expr NL           { printf("%d\n", $1); }
        | error NL          { yyerrok; }
        ;

expr    : TRUE              { $$ = 1; }
        | FALSE             { $$ = 0; }
        | expr OR expr      { $$ = $1 || $3; }
        | expr AND expr     { $$ = $1 && $3; }
        | NOT expr          { $$ = !$2; }
        | '(' expr ')'      { $$ = $2; }
        ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int yylex(void) {
    int c = getchar();
    if (c == EOF) return 0;
    if (c == ' ' || c == '\t') return yylex();
    if (c == '\n') return NL;
    if (c == '(') return '(';
    if (c == ')') return ')';

    // Leer una posible palabra
    if (c >= 'a' && c <= 'z') {
        char buf[10];
        int i = 0;
        buf[i++] = c;
        while ((c = getchar()) >= 'a' && c <= 'z' && i < 9) {
            buf[i++] = c;
        }
        buf[i] = '\0';
        // Devolver el carácter leído de más (si no era letra)
        if (c != EOF && !(c >= 'a' && c <= 'z')) {
            ungetc(c, stdin);
        }
        if (strcmp(buf, "true") == 0) return TRUE;
        if (strcmp(buf, "false") == 0) return FALSE;
        if (strcmp(buf, "and") == 0) return AND;
        if (strcmp(buf, "or") == 0) return OR;
        if (strcmp(buf, "not") == 0) return NOT;
        // Si no es palabra clave, es un token desconocido -> error
        return c; // carácter no reconocido
    }

    // Operadores de un solo carácter (opcional)
    if (c == '&') return AND;
    if (c == '|') return OR;
    if (c == '!') return NOT;

    // Cualquier otro carácter produce error
    return c;
}

int main(void) {
    printf("Calculadora booleana (true/false, and/or/not, Ctrl+D para salir)\n");
    yyparse();
    return 0;
}
