Attribute VB_Name = "Module1"
Sub SplitInto500CellsPerColumn()
  ' modified form http://www.mrexcel.com/forum/excel-questions/678946-split-one-long-column-into-multiple-smaller-columns.html
  Dim X As Long, LastRow As Long, vArrIn As Variant, vArrOut As Variant
  Dim ColumnCount As Long, D As Long
    
  WorkbookName = ActiveWorkbook.Name
    D = CInt(Left(WorkbookName, 2))
    ColumnCount = 50 * D
  LastRow = Cells(Rows.Count, "C").End(xlUp).Row
  vArrIn = Range("C1:C" & LastRow)
  ReDim vArrOut(1 To ColumnCount, 1 To Int(LastRow / ColumnCount) + 1)
  For X = 0 To LastRow - 1
    vArrOut(1 + (X Mod ColumnCount), 1 + Int(X / ColumnCount)) = vArrIn(X + 1, 1)
  Next
  
  Range("D1").Resize(ColumnCount, UBound(vArrOut, 2)) = vArrOut
  
    ' Delete Extra Rows
    RowsRange = (ColumnCount + 1) & ":" & (ColumnCount * 25)
    Rows(RowsRange).EntireRow.Delete
    Columns(1).EntireColumn.Delete
    Columns(2).EntireColumn.Delete
End Sub
