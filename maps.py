from googlemaps import GoogleMaps

mapService = mapService.directions('chicago, il', 'atlanta, ga')

for step in directions['Directions']['Routes'][0]['Steps']:
    print (step['descriptionHtml'])