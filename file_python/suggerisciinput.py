###CARTELLA==prova
def set_color( self, color ):
         '''Check the platform and set the color'''
         if self.platform == 'posix':
                 sys.stdout.write( self.color_syntax + self.color[color] )
                 sys.stderr.write( self.color_syntax + self.color[color] )
         elif self.platform == 'microsoft':
                 WConio.textcolor( self.color[color] )
set_color(self,color)
