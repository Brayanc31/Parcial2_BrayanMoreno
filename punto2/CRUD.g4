grammar CRUD;

// --- REGLAS DEL PARSER ---
programa    : instruccion+ EOF ;

instruccion : operacion (';' | NL) ;

operacion   : create_op
            | read_op
            | update_op
            | delete_op
            ;

create_op   : CREATE '(' ID ',' diccionario ')' ;
read_op     : READ '(' ID ',' diccionario ')' ;
update_op   : UPDATE '(' ID ',' filtro=diccionario ',' datos=diccionario ')' ;
delete_op   : DELETE '(' ID ',' diccionario ')' ;

diccionario : '{' pares? '}' ;
pares       : par (',' par)* ;
par         : STRING ':' valor ;

valor       : STRING
            | NUMBER
            | BOOLEAN
            | diccionario
            ;

// --- REGLAS DEL LEXER ---
CREATE  : 'create' ;
READ    : 'read' ;
UPDATE  : 'update' ;
DELETE  : 'delete' ;

BOOLEAN : 'true' | 'false' ;

ID      : [a-zA-Z_] [a-zA-Z0-9_]* ;
STRING  : '"' ( ~["\r\n\\] | '\\' . )* '"' ;
NUMBER  : '-'? [0-9]+ ('.' [0-9]+)? ;

WS      : [ \t\r\n]+ -> skip ;
