import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
w1=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().push([(39,3)]).rect(26,36).push([(39,2)]).circle(10,mode='s').finalize().extrude(-112).union(w0.sketch().segment((-12,-7),(26,-18)).segment((26,-31)).segment((52,-31)).segment((52,-26)).segment((76,-33)).segment((91,13)).segment((52,25)).segment((52,38)).segment((26,38)).segment((26,33)).segment((2,40)).close().assemble().finalize().extrude(-72)).union(w1.sketch().push([(-78,-27)]).circle(13).circle(11,mode='s').finalize().extrude(-117))