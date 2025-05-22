import cadquery as cq
w0=cq.Workplane('YZ',origin=(-48,0,0))
r=w0.workplane(offset=-6/2).box(198,16,6).union(w0.sketch().rect(96,30).push([(43,-2)]).circle(3,mode='s').finalize().extrude(46)).union(w0.workplane(offset=103/2).box(58,200,103))