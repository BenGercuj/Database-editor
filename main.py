import wx
import wx.adv
import wx.grid

import functions as funcs

class frame_login ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Database login", pos = wx.DefaultPosition, size = wx.Size( 300,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("app.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)             
		
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_loginPnl = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_hostLbl = wx.StaticText( self.m_loginPnl, wx.ID_ANY, u"Host:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        self.m_hostLbl.Wrap( -1 )
        bSizer2.Add( self.m_hostLbl, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_hostTxt = wx.TextCtrl( self.m_loginPnl, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        bSizer2.Add( self.m_hostTxt, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_userLbl = wx.StaticText( self.m_loginPnl, wx.ID_ANY, u"Username:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_userLbl.Wrap( -1 )
        bSizer2.Add( self.m_userLbl, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_userTxt = wx.TextCtrl( self.m_loginPnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_userTxt, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_pwdLbl = wx.StaticText( self.m_loginPnl, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_pwdLbl.Wrap( -1 )
        bSizer2.Add( self.m_pwdLbl, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_pwdTxt = wx.TextCtrl( self.m_loginPnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        bSizer2.Add( self.m_pwdTxt, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_loginStat = wx.StaticText( self.m_loginPnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_loginStat.Wrap( -1 )
        bSizer2.Add( self.m_loginStat, 0, wx.ALL, 5 )
        
        self.m_loginBtn = wx.Button( self.m_loginPnl, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_loginBtn, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_loginPnl.SetSizer( bSizer2 )
        self.m_loginPnl.Layout()
        bSizer2.Fit( self.m_loginPnl )
        self.m_notebook1.AddPage( self.m_loginPnl, u"Login", False )
        self.m_advlogPnl = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_disablesslChk = wx.CheckBox( self.m_advlogPnl, wx.ID_ANY, u"Disable SSL", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_disablesslChk, 0, wx.ALL, 5 )
        
        self.m_emptyLbl = wx.StaticText( self.m_advlogPnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_emptyLbl.Wrap( -1 )
        bSizer3.Add( self.m_emptyLbl, 0, wx.ALL, 5 )
        
        self.m_sslcaLbl = wx.StaticText( self.m_advlogPnl, wx.ID_ANY, u"SSL certificate authority file", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_sslcaLbl.Wrap( -1 )
        bSizer3.Add( self.m_sslcaLbl, 0, wx.ALL, 5 )
        
        self.m_sslcaPck = wx.FilePickerCtrl( self.m_advlogPnl, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer3.Add( self.m_sslcaPck, 0, wx.ALL, 5 )
        
        self.m_emptyLbl1 = wx.StaticText( self.m_advlogPnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_emptyLbl1.Wrap( -1 )
        bSizer3.Add( self.m_emptyLbl1, 0, wx.ALL, 5 )
        
        self.m_enablextrasslChk = wx.CheckBox( self.m_advlogPnl, wx.ID_ANY, u"Enable additional arguments", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_enablextrasslChk, 0, wx.ALL, 5 )
        
        self.m_sslcertLbl = wx.StaticText( self.m_advlogPnl, wx.ID_ANY, u"SSL certificate file", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_sslcertLbl.Wrap( -1 )
        bSizer3.Add( self.m_sslcertLbl, 0, wx.ALL, 5 )
        
        self.m_sslcertPck = wx.FilePickerCtrl( self.m_advlogPnl, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer3.Add( self.m_sslcertPck, 0, wx.ALL, 5 )
        
        self.m_sslkeyLbl = wx.StaticText( self.m_advlogPnl, wx.ID_ANY, u"SSL key file", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_sslkeyLbl.Wrap( -1 )
        bSizer3.Add( self.m_sslkeyLbl, 0, wx.ALL, 5 )
        
        self.m_sslkeyPck = wx.FilePickerCtrl( self.m_advlogPnl, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer3.Add( self.m_sslkeyPck, 0, wx.ALL, 5 )
        
        
        self.m_advlogPnl.SetSizer( bSizer3 )
        self.m_advlogPnl.Layout()
        bSizer3.Fit( self.m_advlogPnl )
        self.m_notebook1.AddPage( self.m_advlogPnl, u"Properties", True )
        
        bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )        
        
        # Events
        self.m_loginBtn.Bind( wx.EVT_BUTTON, self.db_Login )
        self.m_disablesslChk.Bind( wx.EVT_CHECKBOX, self.DisableSSLPck )
        self.m_enablextrasslChk.Bind( wx.EVT_CHECKBOX, self.EnableXtrSSL )
    
    def __del__( self ):
        pass
    
    
    # Event handlers
    def db_Login( self, event ):
        try:
            _host = self.m_hostTxt.GetValue()
            _user = self.m_userTxt.GetValue()
            _pwd = self.m_pwdTxt.GetValue()
            
            self._user_credentials = [_host, _user, _pwd]
            
            if self.m_disablesslChk.IsChecked() == True:
                funcs.sql_login(_host, _user, _pwd)
                
            if self.m_disablesslChk.IsChecked() == False:
                _sslcaPath = self.m_sslcaPck.GetPath()
                funcs.sql_login_ssl(_host, _user, _pwd, _sslcaPath)
                self._user_credentials = [_host, _user, _pwd, _sslcaPath]
                
            if self.m_disablesslChk.IsChecked() == False & self.m_enablextrasslChk.IsChecked() == True:
                _sslcaPath = self.m_sslcaPck.GetPath()
                _sslcertPath = self.m_sslcertPck.GetPath()
                _sslkeyPath = self.m_sslkeyPck.GetPath()
                funcs.sql_login_sslxtra(_host, _user, _pwd, _sslcaPath, _sslcertPath, _sslkeyPath)
                self._user_credentials = [_host, _user, _pwd, _sslcaPath, _sslcertPath, _sslkeyPath]
            
            self.m_loginStat.SetLabel("Login successful")
                      
            frame_main.Show(True)
            
            frame_main.updateData(self._user_credentials)
            frame_main._usrc = self._user_credentials
            
            self.Destroy()
        except:
            self.m_loginStat.SetLabel("Error; unable to log in")
    
    def DisableSSLPck(self, event):
        if self.m_disablesslChk.IsChecked() == True:
            self.m_sslcaPck.Disable()
            self.m_sslcertPck.Disable()
            self.m_sslkeyPck.Disable()
        else:
            self.m_sslcaPck.Enable()
            if self.m_enablextrasslChk.IsChecked() == True:
                self.m_sslcertPck.Enable()
                self.m_sslkeyPck.Enable()
            else:
                self.m_sslcertPck.Disable()
                self.m_sslkeyPck.Disable()
            
    def EnableXtrSSL(self, event):
        if self.m_disablesslChk.IsChecked() == False:
            if self.m_enablextrasslChk.IsChecked() == True:
                self.m_sslcertPck.Enable()
                self.m_sslkeyPck.Enable()
            else:
                self.m_sslcertPck.Disable()
                self.m_sslkeyPck.Disable()
        else:
            pass

class create_movie ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add new entry", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("app.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)   		
		
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_titleCtrl = wx.StaticText( self, wx.ID_ANY, u"Movie title", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_titleCtrl.Wrap( -1 )
        bSizer.Add( self.m_titleCtrl, 0, wx.ALL, 5 )
        
        create_movie.m_titleTxt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( create_movie.m_titleTxt, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_lengthLbl = wx.StaticText( self, wx.ID_ANY, u"Length", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_lengthLbl.Wrap( -1 )
        bSizer.Add( self.m_lengthLbl, 0, wx.ALL, 5 )
        
        self.m_lengthPck = wx.adv.TimePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer.Add(self.m_lengthPck, 0, wx.ALL, 5)
        
        self.m_genre1Lbl = wx.StaticText( self, wx.ID_ANY, u"Genre 1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_genre1Lbl.Wrap( -1 )
        bSizer.Add( self.m_genre1Lbl, 0, wx.ALL, 5 )
        
        self.m_genre1Txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( self.m_genre1Txt, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_genre2Lbl = wx.StaticText( self, wx.ID_ANY, u"Genre 2 (optional)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_genre2Lbl.Wrap( -1 )
        bSizer.Add( self.m_genre2Lbl, 0, wx.ALL, 5 )
        
        self.m_genre2Txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( self.m_genre2Txt, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_directorLbl = wx.StaticText( self, wx.ID_ANY, u"Director", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_directorLbl.Wrap( -1 )
        bSizer.Add( self.m_directorLbl, 0, wx.ALL, 5 )
        
        self.m_directorTxt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( self.m_directorTxt, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_ageLbl = wx.StaticText( self, wx.ID_ANY, u"Age restriction (leave empty if none)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_ageLbl.Wrap( -1 )
        bSizer.Add( self.m_ageLbl, 0, wx.ALL, 5 )
        
        self.m_ageTxt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( self.m_ageTxt, 0, wx.ALL, 5 )
		
        self.m_dIDLbl = wx.StaticText(self, wx.ID_ANY, u"Database ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_dIDLbl.Wrap(-1)
        bSizer.Add(self.m_dIDLbl, 0, wx.ALL, 5)
		
        self.m_dIDTxt = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_dIDTxt.Disable()
        bSizer.Add(self.m_dIDTxt, 0, wx.ALL, 5)
        
        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
        self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
        m_sdbSizer1.Realize();
        
        bSizer.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )
               
        self.SetSizer( bSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.CloseWindow )
        self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.AddEntry )

    def __del__( self ):
        pass
        
    # Event handlers	
    def CloseWindow( self, event ):
        self.Destroy()
    
    def AddEntry( self, event ):
        _hour = str(self.m_lengthPck.GetTime()[0])
        _min = str(self.m_lengthPck.GetTime()[1])
        _sec = str(self.m_lengthPck.GetTime()[2])
        
        if len(_hour) < 2:
            _hour = "0" + _hour
            
        if len(_min) < 2:
            _min = "0" + _min
            
        if len(_sec) < 2:
            _sec = "0" + _sec
        
        _length = _hour + _min + _sec        
        _length = int(_length)
                
        _uc = frame_main._usrc
        
        if len(_uc) == 3:
                _db = funcs.sql_login(_uc[0], _uc[1], _uc[2])
        elif len(_uc) == 4:
                _db = funcs.sql_login_ssl(_uc[0], _uc[1], _uc[2], _uc[3])
        elif len(_uc) == 6:
                _db = funcs.sql_login_sslxtra(_uc[0], _uc[1], _uc[2], _uc[3], _uc[4], _uc[5])
                
        cursor = _db.cursor(buffered=True)
        
        cursor.execute("USE c_internal_sch")  
           
        cmd = ""
        if self.m_dIDTxt.GetValue() != '':
            if self.m_ageTxt.GetValue() != '' and self.m_ageTxt.GetValue() != 'None':
                        cmd = "UPDATE movies SET name = %s, length = %s, genre1 = %s, genre2 = %s, director = %s, age_restriction = %s WHERE (idmovies = %s)"
                        _data = [create_movie.m_titleTxt.GetValue(), _length, self.m_genre1Txt.GetValue(), self.m_genre2Txt.GetValue(), self.m_directorTxt.GetValue(), int(self.m_ageTxt.GetValue()), int(self.m_dIDTxt.GetValue())]
            else:
                        cmd = "UPDATE movies SET name = %s, length = %s, genre1 = %s, genre2 = %s, director = %s, age_restriction = %s WHERE (idmovies = %s)"
                        _data = [create_movie.m_titleTxt.GetValue(), _length, self.m_genre1Txt.GetValue(), self.m_genre2Txt.GetValue(), self.m_directorTxt.GetValue(), None, int(self.m_dIDTxt.GetValue())]
                        			
            cursor.execute(cmd, _data)	

        elif self.m_ageTxt.GetValue() != '':
            _newMovie = (create_movie.m_titleTxt.GetValue(), _length, self.m_genre1Txt.GetValue(), self.m_genre2Txt.GetValue(), self.m_directorTxt.GetValue(), int(self.m_ageTxt.GetValue()))
            cmd = "INSERT INTO movies (name, length, genre1, genre2, director, age_restriction) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(cmd, _newMovie)
        else:
            _newMovie = (create_movie.m_titleTxt.GetValue(), _length, self.m_genre1Txt.GetValue(), self.m_genre2Txt.GetValue(), self.m_directorTxt.GetValue())
            cmd = "INSERT INTO movies (name, length, genre1, genre2, director) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(cmd, _newMovie)
			
        _db.commit()
        
        frame_main.updateData(_uc)	

class frame_main ( wx.Frame ):
    
    def __init__( self, parent ):		
        frame_main._col = 0
        frame_main._row = 0
        frame_main._usrc = []
        
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Main menu", pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("app.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)        
		
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizerMain = wx.BoxSizer( wx.VERTICAL )
        
        self.m_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_moviesPnl = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMovies = wx.BoxSizer( wx.VERTICAL )
        
        frame_main.m_moviesGrd = wx.grid.Grid( self.m_moviesPnl, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,800 ), 0 )
        
        # Grid
        self.m_moviesGrd.CreateGrid( 25, 7 )
        self.m_moviesGrd.EnableEditing( False )
        self.m_moviesGrd.EnableGridLines( True )
        self.m_moviesGrd.EnableDragGridSize( False )
        self.m_moviesGrd.SetMargins( 0, 0 )
        
        # Columns
        self.m_moviesGrd.SetColSize( 0, 630 )
        self.m_moviesGrd.SetColSize( 1, 100 )
        self.m_moviesGrd.SetColSize( 2, 75 )
        self.m_moviesGrd.SetColSize( 3, 75 )
        self.m_moviesGrd.EnableDragColMove( False )
        self.m_moviesGrd.EnableDragColSize( True )
        self.m_moviesGrd.SetColLabelSize( 30 )
        self.m_moviesGrd.SetColLabelValue( 0, u"Title" )
        self.m_moviesGrd.SetColLabelValue( 1, u"Length" )
        self.m_moviesGrd.SetColLabelValue( 2, u"Genre" )
        self.m_moviesGrd.SetColLabelValue( 3, u"Genre 2" )
        self.m_moviesGrd.SetColLabelValue( 4, u"Director" )
        self.m_moviesGrd.SetColLabelValue( 5, u"Age restriction")
        self.m_moviesGrd.SetColLabelValue( 6, u"Database ID")
        self.m_moviesGrd.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        
        # Rows
        self.m_moviesGrd.EnableDragRowSize( False )
        self.m_moviesGrd.SetRowLabelSize( 80 )
        self.m_moviesGrd.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )        
        
        # Cell Defaults
        self.m_moviesGrd.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizerMovies.Add( self.m_moviesGrd, 0, wx.ALL, 5 )
                
        self.m_moviesPnl.SetSizer( bSizerMovies )
        self.m_moviesPnl.Layout()
        bSizerMovies.Fit( self.m_moviesPnl )
        self.m_notebook.AddPage( self.m_moviesPnl, u"Movies", False )
		  
        # Popup menu
        self.popupmenu = wx.Menu()
        
        p_add = self.popupmenu.Append(-1, "Add a new entry")
        self.Bind(wx.EVT_MENU, self.PopupAdd, p_add)
        
        p_remove = self.popupmenu.Append(-1, "Remove an entry")
        self.Bind(wx.EVT_MENU, self.PopupRemove, p_remove)
        
        p_mod = self.popupmenu.Append(-1, "Modify an entry")
        self.Bind(wx.EVT_MENU, self.PopupMod, p_mod)

        p_upd = self.popupmenu.Append(-1, "Update list")
        self.Bind(wx.EVT_MENU, self.PopupUpd, p_upd)        
        
        # Events
        self.m_moviesGrd.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.PopupMenu )
        
        bSizerMain.Add( self.m_notebook, 1, wx.EXPAND |wx.ALL, 5 )
                
        self.SetSizer( bSizerMain )
        self.Layout()
                
        self.Centre( wx.BOTH )      
    
    def updateData(frame_main, _uc):
               
            if len(_uc) == 3:
                _db = funcs.sql_login(_uc[0], _uc[1], _uc[2])
            elif len(_uc) == 4:
                _db = funcs.sql_login_ssl(_uc[0], _uc[1], _uc[2], _uc[3])
            elif len(_uc) == 6:
                _db = funcs.sql_login_sslxtra(_uc[0], _uc[1], _uc[2], _uc[3], _uc[4], _uc[5])
                
            cursor = _db.cursor(buffered=True)
            cursor.execute("USE c_internal_sch")
                
            cursor.execute("SELECT COUNT(name) FROM movies")
            _rows = cursor.fetchone()
            if frame_main.m_moviesGrd.GetNumberRows() < _rows[0]:
                _diff = _rows[0] - frame_main.m_moviesGrd.GetNumberRows()
                frame_main.m_moviesGrd.AppendRows(_diff)
            
            cursor.execute("SELECT name FROM movies")
    
            _entries = 0
            for x in cursor:
                frame_main.m_moviesGrd.SetCellValue(_entries, 0, x[0])
                _entries += 1
                
            cursor.execute("SELECT length FROM movies")
                
            _entries = 0
            for x in cursor:
                frame_main.m_moviesGrd.SetCellValue(_entries, 1, str(x[0]))
                _entries += 1
                
            cursor.execute("SELECT genre1 FROM movies")
                
            _entries = 0
            for x in cursor:
                frame_main.m_moviesGrd.SetCellValue(_entries, 2, str(x[0]))
                _entries += 1
                
            cursor.execute("SELECT genre2 FROM movies")
                
            _entries = 0
            for x in cursor:
                frame_main.m_moviesGrd.SetCellValue(_entries, 3, str(x[0]))
                _entries += 1
                
            cursor.execute("SELECT director FROM movies")
                
            _entries = 0
            for x in cursor:
                frame_main.m_moviesGrd.SetCellValue(_entries, 4, str(x[0]))
                _entries += 1
    
            cursor.execute("SELECT age_restriction FROM movies")
                
            _entries = 0
            for x in cursor:
                frame_main.m_moviesGrd.SetCellValue(_entries, 5, str(x[0]))
                _entries += 1
				
            cursor.execute("SELECT idmovies FROM movies")
                
            _entries = 0
            for x in cursor:
                frame_main.m_moviesGrd.SetCellValue(_entries, 6, str(x[0]))			
                _entries += 1				               
			   
            for x in range(_rows[0], frame_main.m_moviesGrd.GetNumberRows()):
                for y in range(0, 5):
                        frame_main.m_moviesGrd.SetCellValue(x, y, "")
									
    def __del__( self ):
        pass
        
    # Event handlers
    def PopupMenu( self, event ):
        frame_main._col = event.GetCol()
        frame_main._row = event.GetRow()
        
        pos = event.GetPosition()
        self.m_moviesGrd.PopupMenu(self.popupmenu, pos)
        
    def PopupAdd(self, event):
        frame_create = create_movie(None)                        
        frame_create.Show(True)
    
    def PopupRemove(self, event):        
            if len(frame_main._usrc) == 3:
                _db = funcs.sql_login(frame_main._usrc[0],frame_main._usrc[1], frame_main._usrc[2])
            elif len(frame_main._usrc) == 4:
                _db = funcs.sql_login_ssl(frame_main._usrc[0], frame_main._usrc[1], frame_main._usrc[2], frame_main._usrc[3])
            elif len(frame_main._usrc) == 6:
                _db = funcs.sql_login_sslxtra(frame_main._usrc[0], frame_main._usrc[1], frame_main._usrc[2], frame_main._usrc[3], frame_main._usrc[4], frame_main._usrc[5])

            cursor = _db.cursor(buffered=True)
            cursor.execute("USE c_internal_sch")
			
            cmd = "DELETE FROM movies WHERE idmovies = %s"
            _id = (frame_main.m_moviesGrd.GetCellValue(frame_main._row, 6), )
			
            cursor.execute(cmd, _id)
            _db.commit()
            
            frame_main.updateData(frame_main._usrc)
			    
    def PopupUpd(self, event):
        frame_main.updateData(frame_main._usrc)
	
    def PopupMod(self, event):	
            if frame_main.m_moviesGrd.GetCellValue(frame_main._row, 6) != '':
                frame_create = create_movie(None)
		
                frame_create.m_titleTxt.SetValue(frame_main.m_moviesGrd.GetCellValue(frame_main._row, 0))
	        
                _timestr = frame_main.m_moviesGrd.GetCellValue(frame_main._row, 1)
                _time = _timestr.split(":")
                frame_create.m_lengthPck.SetTime(int(_time[0]), int(_time[1]), int(_time[2]))
	        
                frame_create.m_genre1Txt.SetValue(frame_main.m_moviesGrd.GetCellValue(frame_main._row, 2))
                frame_create.m_genre2Txt.SetValue(frame_main.m_moviesGrd.GetCellValue(frame_main._row, 3))
	        
                frame_create.m_directorTxt.SetValue(frame_main.m_moviesGrd.GetCellValue(frame_main._row, 4))        
                frame_create.m_ageTxt.SetValue(frame_main.m_moviesGrd.GetCellValue(frame_main._row, 5))
	        
                frame_create.m_dIDTxt.SetValue(frame_main.m_moviesGrd.GetCellValue(frame_main._row, 6))		
                frame_create.Show(True)
            else:
                pass

main = wx.App()

frame_main = frame_main(None)
frame_login = frame_login(None)

frame_main.Show(False)
frame_login.Show(True)
main.MainLoop()