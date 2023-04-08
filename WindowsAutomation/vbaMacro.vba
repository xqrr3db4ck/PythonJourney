Sub ProcesoCompleto()
Hoja1.Activate
Call Eliminar
Call TraducirPlastico
Call TraducirContenidoBNCL
Call TraducirContenido
Call TraducirTapa
Call TraducirEncaratulado
Call AjustarAncho
Call Bordes
Call columnaguion
Call contarpapel


End Sub

Sub Eliminar()
Range("C:C").Columns.Delete
Range("C:C").Columns.Delete
Range("C:C").Columns.Delete
Range("B:B").Columns.Delete
Range("D:D").Columns.Delete
Range("D:D").Columns.Delete
Range("L:L").Columns.Delete
Range("L:M").Columns.Delete
End Sub

Sub TraducirPlastico()
Dim i As Integer
Dim j As Integer

While Cells(1 + j, 1) <> ""
j = j + 1
Wend

For i = 1 To j
    If Cells(i, 11) = "LAMMAT" Then
        Cells(i, 11) = "MATE"
        Cells(i, 11).Interior.Color = RGB(133, 193, 233)
    ElseIf Cells(i, 11) = "LAMBTE" Then
        Cells(i, 11) = "BRILLANTE"
   End If
Next i

End Sub

Sub TraducirContenidoBNCL()
Dim i As Integer
Dim j As Integer

While Cells(1 + j, 1) <> ""
j = j + 1
Wend

For i = 1 To j
    If Cells(i, 7) = "CL" Then
        Cells(i, 7) = "Color"
        Cells(i, 7).Interior.Color = RGB(133, 193, 233)
   End If
Next i

End Sub

Sub TraducirContenido()
Dim i As Integer
Dim j As Integer

While Cells(1 + j, 1) <> ""
j = j + 1
Wend

For i = 1 To j
    If Cells(i, 8) = "BNAHU080" Then
        Cells(i, 8) = "HOLMEN55"
    ElseIf Cells(i, 8) = "BNOBR080" Then
        Cells(i, 8) = "BOND70"
    ElseIf Cells(i, 8) = "COOBR090" Then
        Cells(i, 8) = "BOND70"
   ElseIf Cells(i, 8) = "BNOBR090" Then
        Cells(i, 8) = "BOND90"
   ElseIf Cells(i, 8) = "BNILM115" Then
        Cells(i, 8) = "ESM115"
    End If
Next i

End Sub

Sub TraducirTapa()
Dim i As Integer
Dim j As Integer

While Cells(1 + j, 1) <> ""
j = j + 1
Wend

For i = 1 To j
    If Cells(i, 9) = "TAILU270" Then
        Cells(i, 9) = "ESM. 300"
    End If
Next i

End Sub

Sub TraducirEncaratulado()
Dim i As Integer
Dim j As Integer

While Cells(1 + j, 1) <> ""
j = j + 1
Wend

For i = 1 To j
    If Cells(i, 10) = "ENCBIN" Then
        Cells(i, 10) = "RUSTICO"
    ElseIf Cells(i, 10) = "ENCACA" Then
        Cells(i, 10) = "CABALLETE"
    End If
Next i

End Sub

Sub AjustarAncho()

Range("A2:A2").ColumnWidth = 20
Range("B2:B2").ColumnWidth = 15
Range("C2:C2").ColumnWidth = 20
Range("D2:D2").ColumnWidth = 10
Range("E2:E2").ColumnWidth = 10
Range("F2:F2").ColumnWidth = 10
Range("G2:G2").ColumnWidth = 10
Range("H2:H2").ColumnWidth = 10
Range("I2:I2").ColumnWidth = 15
Range("J2:J2").ColumnWidth = 15
Range("A1:A1000").RowHeight = 30
Range("A1:N1").Interior.Color = RGB(100, 140, 280)
End Sub

Sub Bordes()

Dim i As Integer
Dim j As Integer

While Cells(1 + j, 1) <> ""
j = j + 1
Wend

For i = 1 To j
For y = 1 To 14
Cells(i, y).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Next y
Next i
End Sub

Sub EliminarTODO()
Hoja1.Activate
Range("A2:Q2").Columns.Delete
Range("A1:A1000").Columns.Delete

i = 1
While Cells(1, 1) <> ""
Range(Cells(1, 1), Cells(1000, i)).Columns.Delete
Wend


i = 1
j = 0
While j <> 30
Range(Cells(1, 1), Cells(1000, i)).ColumnWidth = 10
i = i + 1
j = j + 1
Wend

Range("A1:A1000").RowHeight = 12.75
Range("A1:F1000").Columns.Delete

End Sub

Sub columnaguion()
'INSERTA EL NUMERO DE LA IZQUIERDA Y LOS GUIONES

Columns(4).Insert
Columns(1).Insert , xlFormatFromRightOrBelow
Range("E2:E2").ColumnWidth = 1
Range("A2:A2").ColumnWidth = 3

'PARA LLENAR LOS ESPACIOS VACIOS

Dim i As Integer
Dim j As Integer

While Cells(1 + j, 2) <> ""
j = j + 1
Wend

For i = 1 To j
    If Cells(i, 5) = "" Then
        Cells(i, 5) = "-"
      End If
      If Cells(i, 1) = "" Then
        Cells(i, 1) = i - 1
      End If
Next i


End Sub

Sub contarpapel()
'SE ESTABLECE LA VARIABLE

Dim BOND70M As Double

Dim HOLMEN55M As Double

Dim BOND90M As Double

Dim BOND70 As Double

Dim HOLMEN55 As Double

Dim BOND90 As Double

Dim k As Integer
Dim v As Integer

'SUMA LA CANTIDAS DE PAGINAS Y LIBROS QUE HAY SEGUN EL SUSTRATO


While Cells(1 + k, 1) <> ""
k = k + 1
Wend

For i = 1 To k

If Cells(i, 10) = "BOND70" And Cells(i, 8) >= "170x240" Then
        BOND70M = Application.WorksheetFunction.RoundUp(BOND70M + ((Cells(i, 7) * Cells(i, 6))), 0)
        
ElseIf Cells(i, 10) = "HOLMEN55" And Cells(i, 8) >= "170x240" Then
        HOLMEN55M = Application.WorksheetFunction.RoundUp(HOLMEN55M + ((Cells(i, 7) * Cells(i, 6))), 0)
        
ElseIf Cells(i, 10) = "BOND90" And Cells(i, 8) >= "170x240" Then
        BOND90M = Application.WorksheetFunction.RoundUp(BOND90M + ((Cells(i, 7) * Cells(i, 6))), 0)
        
''''''''''''''--------------------

ElseIf Cells(i, 10) = "BOND70" And Cells(i, 8) < "170x240" Then
        BOND70 = Application.WorksheetFunction.RoundUp(BOND70 + ((Cells(i, 7) * Cells(i, 6))), 0)
        
ElseIf Cells(i, 10) = "HOLMEN55" And Cells(i, 8) < "170x240" Then
        HOLMEN55 = Application.WorksheetFunction.RoundUp(HOLMEN55 + ((Cells(i, 7) * Cells(i, 6))), 0)
        
ElseIf Cells(i, 10) = "BOND90" And Cells(i, 8) < "170x240" Then
        BOND90 = Application.WorksheetFunction.RoundUp(BOND90 + ((Cells(i, 7) * Cells(i, 6))), 0)
   End If
   
Next i
'DIVIDIR EL RESULTADO



 BOND70M = Application.WorksheetFunction.RoundUp(BOND70M / 16, 0)
 HOLMEN55M = Application.WorksheetFunction.RoundUp(HOLMEN55M / 16, 0)
 BOND90M = Application.WorksheetFunction.RoundUp(BOND90M / 16, 0)
 BOND70 = Application.WorksheetFunction.RoundUp(BOND70 / 32, 0)
 HOLMEN55 = Application.WorksheetFunction.RoundUp(HOLMEN55 / 32, 0)
 BOND90 = Application.WorksheetFunction.RoundUp(BOND90 / 32, 0)

v = 3

'TABLA DE CANTIDADES TOTALES

Cells(k + 2, 2) = "PAPELES"
Cells(k + 2, 3) = "CANTIDAD"
Cells(k + 2, 4) = "PLIEGO"
Cells(k + 2, 5) = "*"
Cells(k + 2, 6) = "T.CORTE"



'INTENTO SEPRACION DE TAMANOS DE PAPEL
If HOLMEN55M <> 0 Then
Cells(k + v, 2) = "HOLMEN 55grs"
Cells(k + v, 3) = HOLMEN55M
Cells(k + v, 4) = "70x100"
Cells(k + v, 5) = "-"
Cells(k + v, 6) = "50X35"
Cells(k + v, 2).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 3).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 4).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 5).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 6).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
v = v + 1
End If

If HOLMEN55 <> 0 Then
Cells(k + v, 2) = "HOLMEN 55grs"
Cells(k + v, 3) = HOLMEN55
Cells(k + v, 4) = "70x100"
Cells(k + v, 5) = "-"
Cells(k + v, 6) = "35X25"
Cells(k + v, 2).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 3).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 4).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 5).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 6).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
v = v + 1
End If

If BOND70M <> 0 Then
Cells(k + v, 2) = "BOND 70grs"
Cells(k + v, 3) = BOND70M
Cells(k + v, 4) = "70x100"
Cells(k + v, 5) = "-"
Cells(k + v, 6) = "50X35"
Cells(k + v, 2).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 3).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 4).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 5).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 6).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
v = v + 1
End If

If BOND70 <> 0 Then
Cells(k + v, 2) = "BOND 70grs"
Cells(k + v, 3) = BOND70
Cells(k + v, 4) = "70x100"
Cells(k + v, 5) = "-"
Cells(k + v, 6) = "35X25"
Cells(k + v, 2).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 3).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 4).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 5).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 6).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
v = v + 1
End If


If BOND90M <> 0 Then
Cells(k + v, 2) = "BOND 90grs"
Cells(k + v, 3) = BOND90M
Cells(k + v, 4) = "70x100"
Cells(k + v, 5) = "-"
Cells(k + v, 6) = "50X35"
Cells(k + v, 2).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 3).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 4).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 5).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 6).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
v = v + 1
End If


If BOND90 <> 0 Then
Cells(k + v, 2) = "BOND 90grs"
Cells(k + v, 3) = BOND90
Cells(k + v, 4) = "70x100"
Cells(k + v, 5) = "-"
Cells(k + v, 6) = "35X25"
Cells(k + v, 2).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 3).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 4).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 5).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + v, 6).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
v = v + 1
End If


'CREAR CUADRICULA Y INSERTAR COLOR

Cells(k + 2, 2).Interior.Color = RGB(100, 140, 280)
Cells(k + 2, 3).Interior.Color = RGB(100, 140, 280)
Cells(k + 2, 4).Interior.Color = RGB(100, 140, 280)
Cells(k + 2, 5).Interior.Color = RGB(100, 140, 280)
Cells(k + 2, 6).Interior.Color = RGB(100, 140, 280)
Cells(k + 2, 2).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + 2, 3).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + 2, 4).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + 2, 5).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2
Cells(k + 2, 6).BorderAround LineStyle:=xlContinuous, ColorIndex:=1, Weight:=2


Cells(1, 1) = ""

End Sub
