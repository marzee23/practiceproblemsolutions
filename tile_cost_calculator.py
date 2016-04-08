#!/usr/bin/env python3

#Find Cost of Tile to Cover W x L Floor
#Calculate the total cost of tile it would take to cover a floor plan of width and height

from math import ceil
import unittest

def calculate_tiles_for_side(measurement_meters, tile_size_cm):
    measurement_centimeters = measurement_meters * 100
    return ceil(measurement_centimeters / tile_size_cm)

def calculate_tiles_needed(length , width, tile_size):
    length_tiles = calculate_tiles_for_side(length, tile_size)
    width_tiles = calculate_tiles_for_side(width, tile_size)
    return length_tiles * width_tiles

def calculate_tile_price(number_of_tiles, pricing_structure):
    if isinstance(price_per_tile, int):
        return calculate_tile_price_basic(number_of_tiles, pricing_structure)
    elif isinstance(price_per_til, list):
        return calculate_tile_price_basic(number_of_tiles, pricing_structure)
    else:
        raise ValueError("Expected int or list of tuples")

def calculate_tile_price_basic(number_of_tiles, price_per_tile):
    return number_of_tiles * price_per_tile

def calculate_tile_price_structured(number_of_tiles, pricing_structure):
    """
    Challenge!

    Try to make this function allow quantity breaks
    i.e.
        up to 100 tiles:  $3.00
        up to 1000 tiles: $2.75
        1000+ tiles:      $2.50
    """
    pass

class TestTileCalculator(unittest.TestCase):
    test_pricing_structure = [
        (0, 3.00),
        (100, 2.75),
        (1000, 2.50),
    ]    

    def test_calculate_tiles_for_side(self):
        tiles_calculated = calculate_tiles_for_side(1,10)
        self.assertEqual(tiles_calculated,10)
        tiles_calculated = calculate_tiles_for_side(1.02,10)
        self.assertEqual(tiles_calculated, 11)

    def test_caclulate_needed_tiles_works(self):
        tiles_needed = calculate_tiles_needed(1,1,10)
        self.assertEqual(tiles_needed,100)
        tiles_needed = calculate_tiles_needed(1.02,1,10)
        self.assertEqual(tiles_needed,110)
        tiles_needed = calculate_tiles_needed(1.02,1.02,10)
        self.assertEqual(tiles_needed,121)

    def test_calculate_tile_price_basic(self):
        tile_price = calculate_tile_price_basic(100,3.01)
        self.assertEqual(tile_price,301.00)
    
    def test_calculate_tile_price_valueerror(self):
        self.assertraises(ValueError, calculate_tile_price(10, {}))

    def test_calculate_tile_price_with_basic_pricing(self):
        tile_price = calculate_tile_price_basic(100,3.01)
        self.assertEqual(tile_price,301.00)

    def test_calculate_tile_price_structured(self):            
        calculate_tile_price(10,test_pricing_structure)
  
    def test_calculate_tile_price_structured(self):
        tile_price = calculate_tile_price_structured(1,test_pricing_structure)
        self.assertEquals(tile_price, 3.00)
        
        tile_price = calculate_tile_price_structured(100, test_pricing_structure)
        self.assertEqual(tile_price, 100*3.00)

        tile_price = calculate_tile_price_structured(101,test_pricing_structure)
        self.assertEquals(tile_price, 101*2.75)

        tile_price = calculate_tile_price_structured(1001, test_pricing_structure)
        self.assertEquals(tile_price, 1001*2.50)     



if __name__ == '__main__':
    unittest.main()
