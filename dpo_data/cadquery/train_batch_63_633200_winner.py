import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
w1=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.sketch().segment((-100,-19),(-19,-19)).segment((-19,0)).segment((22,-78)).segment((100,-40)).segment((55,52)).segment((-19,16)).segment((-19,42)).segment((-35,42)).segment((-35,52)).segment((21,67)).segment((17,78)).segment((-44,56)).segment((-39,42)).segment((-100,42)).close().assemble().finalize().extrude(82).union(w1.sketch().segment((24,-78),(26,-78)).segment((26,-76)).segment((24,-76)).arc((25,-77),(24,-78)).assemble().finalize().extrude(84))