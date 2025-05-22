import cadquery as cq
w0=cq.Workplane('YZ',origin=(75,0,0))
r=w0.sketch().rect(46,200).push([(2,91)]).circle(8,mode='s').finalize().extrude(-151)