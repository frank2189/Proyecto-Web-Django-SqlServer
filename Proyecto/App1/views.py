from django.shortcuts import render
from django.db import connection

##Funcion para que nos lleve a la pagina principal
def home(request):

    return render(request, 'home.html')

##Funcion que nos muestra la consulta #1
def mostrarConsulta1(request):

    first_name = "John"

    Consulta1= """

    SELECT top (10000)
            DC.FirstName + ' ' + DC.LastName AS Name,
            DC.BirthDate,
            DATEDIFF(YEAR, DC.BirthDate, '2010-01-01') AS Age,
            DC.MaritalStatus,
            DC.Gender,
            DC.TotalChildren,
            DC.Education,
            DC.Occupation,
            DC.CustomerType,
            DG.StateProvinceName,
            DG.RegionCountryName
    FROM
        [dbo].[DimCustomer] AS DC
    JOIN
        [dbo].[DimGeography] AS DG ON DC.GeographyKey = DG.GeographyKey
    WHERE
        FirstName = %s AND DC.FirstName IS NOT NULL;
        --FirstName IS NOT NULL;"""

    with connection.cursor() as cursor:
        cursor.execute(Consulta1,[first_name])
        ##cursor.execute(Consulta1)
        resultados = cursor.fetchall()
    return render(request,'template1.html',{'resultados': resultados})

##Funcion que nos muestra la consulta #2
def mostrarConsulta2(request):

    brand = "Contoso"

    Consulta2 ="""
    SELECT TOP(10000)    
            P.ProductName,     
            P.BrandName,     
            P.ClassName,     
            FORMAT(P.UnitPrice, 'C', 'en-US') AS UnitPrice,     
            FORMAT(P.UnitCost, 'C', 'en-US') AS UnitCost,     
            FORMAT(P.UnitPrice - P.UnitCost, 'C', 'en-US') AS [Margen Ganancia],    
            P.Status,     S.StoreName,    
            FI.SafetyStockQuantity
    FROM dbo.FactInventory FI
    INNER JOIN dbo.DimProduct P ON FI.ProductKey = P.ProductKey
    INNER JOIN DimStore S ON S.StoreKey = FI.StoreKey
    --WHERE P.Status IS NOT NULL;
    WHERE BrandName = %s AND P.Status IS NOT NULL;"""

    with connection.cursor() as cursor:
        ##cursor.execute(Consulta2)
        cursor.execute(Consulta2,[brand])
        resultados = cursor.fetchall()
    return render(request,'template2.html',{'resultados': resultados})
