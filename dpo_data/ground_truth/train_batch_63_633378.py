import cadquery as cq
w0=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.sketch().segment((-96,38),(-26,-100)).segment((96,-38)).segment((26,100)).segment((-18,78)).segment((29,78)).segment((29,60)).segment((-19,60)).segment((-19,77)).close().assemble().finalize().extrude(37)