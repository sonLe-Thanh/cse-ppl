from MPVisitor import MPVisitor
from MPParser import MPParser

class Count(MPVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return 2 + sum([1+ self.visitDecl(x) for x in ctx.decl()])


    # Visit a parse tree produced by MPParser#decl.
    def visitDecl(self, ctx:MPParser.DeclContext):
        return self.visitFuncdecl(ctx.funcdecl()) if ctx.funcdecl() else self.visitProcdecl(ctx.procdecl())


    # Visit a parse tree produced by MPParser#procdecl.
    def visitProcdecl(self, ctx:MPParser.ProcdeclContext):
        return 6 + self.visitBody(ctx.body())


    # Visit a parse tree produced by MPParser#funcdecl.
    def visitFuncdecl(self, ctx:MPParser.FuncdeclContext):
        return 7 + self.visitMtype(ctx.mtype()) + self.visitBody(ctx.body())


    # Visit a parse tree produced by MPParser#body.
    def visitBody(self, ctx:MPParser.BodyContext):
        return 3 + (self.visitStmt(ctx.stmt()) if ctx.stmt() else 0)


    # Visit a parse tree produced by MPParser#stmt.
    def visitStmt(self, ctx:MPParser.StmtContext):
        return 2 + self.visitFuncall(ctx.funcall())


    # Visit a parse tree produced by MPParser#funcall.
    def visitFuncall(self, ctx:MPParser.FuncallContext):
        return 4 + (self.visitExp(ctx.exp()) if ctx.exp() else 0)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return 2


    # Visit a parse tree produced by MPParser#mtype.
    def visitMtype(self, ctx:MPParser.MtypeContext):
        return 2