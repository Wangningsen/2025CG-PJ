import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-32))
r=w0.sketch().arc((-34,1),(-84,-76),(8,-63)).arc((10,-65),(11,-68)).segment((23,-74)).segment((23,-72)).arc((15,-76),(6,-79)).arc((8,-74),(8,-69)).arc((10,-70),(11,-73)).segment((21,-79)).segment((24,-73)).segment((9,-66)).arc((9,-50),(6,-34)).arc((66,86),(-34,1)).assemble().finalize().extrude(63)