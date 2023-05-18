import FreeCAD as App
import Draft
import Part

def squarePoints(p0, height, width):
	# Points for the base
	p1 = (p0[0], p0[1], p0[2])
	p2 = (p0[0], p0[1] + height, p0[2])
	p3 = (p0[0] + width, p0[1] + height, p0[2])
	p4 = (p0[0] + width, p0[1], p0[2])
	
	return [p1, p2, p3, p4]
 
def createPocket(sketch, pad, body, t):
	pocket = body.newObject('PartDesign::Pocket','Pocket')
	pocket.Profile = sketch
	pocket.Length = t
	
	doc.recompute()

def sketchSquare(coords, body, doc, sketch_name):
	p1, p2, p3, p4 = coords[0], coords[1], coords[2], coords[3]
	sketch = body.newObject("Sketcher::SketchObject", sketch_name)
	sketch.MapMode = 'FlatFace'
	sketch.addGeometry(Part.LineSegment(
				App.Vector(p1),
				App.Vector(p2)), False)
	sketch.addGeometry(Part.LineSegment(
				App.Vector(p2),
				App.Vector(p3)), False)
	sketch.addGeometry(Part.LineSegment(
				App.Vector(p3),
				App.Vector(p4)), False)
	sketch.addGeometry(Part.LineSegment(
				App.Vector(p4),
				App.Vector(p1)), False)

	return sketch

def padSketch(body, sketch, pad_t, doc):
	
	pad = body.newObject('PartDesign::Pad','Pad')
	pad.Profile = sketch
	pad.Length = pad_t
	doc.recompute()
	return pad

def createHole(coords, hole_radius, body, pad, doc):
	pad_faces = pad.Shape.Faces
	hole_sketch = body.newObject('Sketcher::SketchObject','holeSketch')
	hole_sketch.Support = (pad,['Face6',])
	hole_sketch.MapMode = 'FlatFace'
	hole_sketch.addGeometry(Part.Circle(App.Vector(coords),App.Vector(0,0,1),hole_radius),False)

# Main
doc_path = r"C:\Users\oskari.oksanen\opettelua\freecad_ohjelmat\ohutlevy.FCStd"
doc = App.openDocument(doc_path)
#doc1 = App.ActiveDocument

# Parameters
height = 100
width = 250
thickness = 30
p0 = (0, 0, 0)
sheet_coords = squarePoints(p0, height, width)

sheet_body = doc.addObject('PartDesign::Body','Body')
sheet_sketch = sketchSquare(sheet_coords,sheet_body, doc, "bodySketch")
sheet_sketch.Support = (doc.getObject( 'XY_Plane'))
sheet_pad =  padSketch(sheet_body, sheet_sketch, thickness, doc)

# Points for the hole
hole_height = 50
hole_width = 100
hole_p0 = (75, 25, 0)
hole_coords = squarePoints(hole_p0, hole_height, hole_width)

sheet_faces =sheet_pad.Shape.Faces
hole_sketch = sketchSquare(hole_coords, sheet_body, doc, "hole1Sketch")
hole_sketch.Support = (sheet_pad,['Face6',])
createPocket(hole_sketch, sheet_pad, sheet_body, thickness)

# Save the document
doc.save()
