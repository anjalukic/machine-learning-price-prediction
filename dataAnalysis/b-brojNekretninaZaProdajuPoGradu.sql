select count(id) as 'broj nekretnina za prodaju' ,location as 'grad' from realestatecopy where forSale = 1 group by location