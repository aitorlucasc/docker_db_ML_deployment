select country, year(InvoiceDate) as "year", month(InvoiceDate) as "month"  , sum(UnitPrice*Quantity) as price
from retail
where year(InvoiceDate) = 2011 and Country = "United Kingdom"
group by 1,2,3
order by 3;