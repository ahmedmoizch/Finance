-- To query holdings with respect to user id with inner join
SELECT 
    holdings.asset_symbol, 
    holdings.asset_quantity, 
    holdings.buy_price, 
    psx_cache.Current 
FROM holdings
INNER JOIN psx_cache ON holdings.asset_symbol = psx_cache.symbol
where holdings.user_id = 1;