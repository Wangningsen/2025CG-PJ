import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
r=w0.sketch().segment((-59,-85),(59,-85)).segment((59,-75)).segment((7,-79)).segment((5,-49)).segment((16,-34)).segment((43,-31)).arc((49,-26),(59,-23)).segment((59,85)).segment((-59,85)).close().assemble().finalize().extrude(-161).union(w0.workplane(offset=39/2).cylinder(39,32))