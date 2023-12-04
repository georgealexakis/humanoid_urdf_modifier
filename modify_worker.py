import lxml.etree as ET

def get_humanoid_urdf(urdf = 'factory_worker.urdf'):
    # Parse the URDF file
    tree = ET.parse('./workers/' + str(urdf))
    root = tree.getroot()
    # Data arrays
    body_part_length = []
    body_part_radius = []
    body_part_mass = []

    # Collision element for the left_upper_arm
    left_upper_arm_collision = root.find(f".//link[@name='left_upper_arm']/collision")
    left_upper_arm_length = left_upper_arm_collision.find('geometry').find('capsule').get('length')
    left_upper_arm_radius = left_upper_arm_collision.find('geometry').find('capsule').get('radius')
    left_upper_arm_mass = root.find(f".//link[@name='left_upper_arm']/inertial").find('mass').get('value')
    body_part_length.append(left_upper_arm_length)
    body_part_radius.append(left_upper_arm_radius)
    body_part_mass.append(left_upper_arm_mass)

    # Collision element for the left_lower_arm
    left_lower_arm_collision = root.find(f".//link[@name='left_lower_arm']/collision")
    left_lower_arm_length = left_lower_arm_collision.find('geometry').find('capsule').get('length')
    left_lower_arm_radius = left_lower_arm_collision.find('geometry').find('capsule').get('radius')
    left_lower_arm_mass = root.find(f".//link[@name='left_lower_arm']/inertial").find('mass').get('value')
    body_part_length.append(left_lower_arm_length)
    body_part_radius.append(left_lower_arm_radius)
    body_part_mass.append(left_lower_arm_mass)

    # Collision element for the left_wristpalm
    left_wristpalm_collision = root.find(f".//link[@name='left_wristpalm']/collision")
    left_wristpalm_length = left_wristpalm_collision.find('geometry').find('capsule').get('length')
    left_wristpalm_radius = left_wristpalm_collision.find('geometry').find('capsule').get('radius')
    left_wristpalm_mass = root.find(f".//link[@name='left_wristpalm']/inertial").find('mass').get('value')
    body_part_length.append(left_wristpalm_length)
    body_part_radius.append(left_wristpalm_radius)
    body_part_mass.append(left_wristpalm_mass)

    # Collision element for the right_upper_arm
    right_upper_arm_collision = root.find(f".//link[@name='right_upper_arm']/collision")
    right_upper_arm_length = right_upper_arm_collision.find('geometry').find('capsule').get('length')
    right_upper_arm_radius = right_upper_arm_collision.find('geometry').find('capsule').get('radius')
    right_upper_arm_mass = root.find(f".//link[@name='right_upper_arm']/inertial").find('mass').get('value')
    body_part_length.append(right_upper_arm_length)
    body_part_radius.append(right_upper_arm_radius)
    body_part_mass.append(right_upper_arm_mass)

    # Collision element for the right_lower_arm
    right_lower_arm_collision = root.find(f".//link[@name='right_lower_arm']/collision")
    right_lower_arm_length = right_lower_arm_collision.find('geometry').find('capsule').get('length')
    right_lower_arm_radius = right_lower_arm_collision.find('geometry').find('capsule').get('radius')
    right_lower_arm_mass = root.find(f".//link[@name='right_lower_arm']/inertial").find('mass').get('value')
    body_part_length.append(right_lower_arm_length)
    body_part_radius.append(right_lower_arm_radius)
    body_part_mass.append(right_lower_arm_mass)

    # Collision element for the right_wristpalm
    right_wristpalm_collision = root.find(f".//link[@name='right_wristpalm']/collision")
    right_wristpalm_length = right_wristpalm_collision.find('geometry').find('capsule').get('length')
    right_wristpalm_radius = right_wristpalm_collision.find('geometry').find('capsule').get('radius')
    right_wristpalm_mass = root.find(f".//link[@name='right_wristpalm']/inertial").find('mass').get('value')
    body_part_length.append(right_wristpalm_length)
    body_part_radius.append(right_wristpalm_radius)
    body_part_mass.append(right_wristpalm_mass)

    # Collision element for the left_thigh
    left_thigh_collision = root.find(f".//link[@name='left_thigh']/collision")
    left_thigh_length = left_thigh_collision.find('geometry').find('capsule').get('length')
    left_thigh_radius = left_thigh_collision.find('geometry').find('capsule').get('radius')
    left_thigh_mass = root.find(f".//link[@name='left_thigh']/inertial").find('mass').get('value')
    body_part_length.append(left_thigh_length)
    body_part_radius.append(left_thigh_radius)
    body_part_mass.append(left_thigh_mass)

    # Collision element for the left_shin
    left_shin_collision = root.find(f".//link[@name='left_shin']/collision")
    left_shin_length = left_shin_collision.find('geometry').find('capsule').get('length')
    left_shin_radius = left_shin_collision.find('geometry').find('capsule').get('radius')
    left_shin_mass = root.find(f".//link[@name='left_shin']/inertial").find('mass').get('value')
    body_part_length.append(left_shin_length)
    body_part_radius.append(left_shin_radius)
    body_part_mass.append(left_shin_mass)

    # Collision element for the left_foot
    left_foot_collision = root.find(f".//link[@name='left_foot']/collision")
    left_foot_length = left_foot_collision.find('geometry').find('capsule').get('length')
    left_foot_radius = left_foot_collision.find('geometry').find('capsule').get('radius')
    left_foot_mass = root.find(f".//link[@name='left_foot']/inertial").find('mass').get('value')
    body_part_length.append(left_foot_length)
    body_part_radius.append(left_foot_radius)
    body_part_mass.append(left_foot_mass)

    # Collision element for the right_thigh
    right_thigh_collision = root.find(f".//link[@name='right_thigh']/collision")
    right_thigh_length = right_thigh_collision.find('geometry').find('capsule').get('length')
    right_thigh_radius = right_thigh_collision.find('geometry').find('capsule').get('radius')
    right_thigh_mass = root.find(f".//link[@name='right_thigh']/inertial").find('mass').get('value')
    body_part_length.append(right_thigh_length)
    body_part_radius.append(right_thigh_radius)
    body_part_mass.append(right_thigh_mass)

    # Collision element for the right_shin
    right_shin_collision = root.find(f".//link[@name='right_shin']/collision")
    right_shin_length = right_shin_collision.find('geometry').find('capsule').get('length')
    right_shin_radius = right_shin_collision.find('geometry').find('capsule').get('radius')
    right_shin_mass = root.find(f".//link[@name='right_shin']/inertial").find('mass').get('value')
    body_part_length.append(right_shin_length)
    body_part_radius.append(right_shin_radius)
    body_part_mass.append(right_shin_mass)

    # Collision element for the right_foot
    right_foot_collision = root.find(f".//link[@name='right_foot']/collision")
    right_foot_length = right_foot_collision.find('geometry').find('capsule').get('length')
    right_foot_radius = right_foot_collision.find('geometry').find('capsule').get('radius')
    right_foot_mass = root.find(f".//link[@name='right_foot']/inertial").find('mass').get('value')
    body_part_length.append(right_foot_length)
    body_part_radius.append(right_foot_radius)
    body_part_mass.append(right_foot_mass)

    return body_part_length, body_part_radius, body_part_mass

def set_humanoid_urdf(body_part_length, body_part_radius, body_part_mass, urdf = 'factory_worker.urdf'):
    # Parse the URDF file
    tree = ET.parse('./workers/' + str(urdf))
    root = tree.getroot()

    # Collision element for the left_upper_arm
    left_upper_arm_collision = root.find(f".//link[@name='left_upper_arm']/collision")
    left_upper_arm_collision.find('geometry').find('capsule').set('length', body_part_length[0])
    left_upper_arm_collision.find('geometry').find('capsule').set('radius', body_part_radius[0])
    root.find(f".//link[@name='left_upper_arm']/inertial").find('mass').set('value', body_part_mass[0])
    
    # Joint of left_upper_arm
    x = '0.00000'
    y = '0.00000'
    temp = -round(float(body_part_length[0])/2 - 0.06, 5)
    z = str(temp)
    # Collision element for the link
    root.find(f".//joint[@name='jointfix_13_35']").find('origin').set('xyz', f"{x} {y} {z}")

    # Joint of left_elbow
    x = '0.03000'
    y = '0.00000'
    temp = -(0.2 + round(float(body_part_length[0])/2, 5) - 0.06)
    z = str(temp)
    # Collision element for the link
    root.find(f".//joint[@name='left_elbow']").find('origin').set('xyz', f"{x} {y} {z}")

    # Collision element for the left_lower_arm
    left_lower_arm_collision = root.find(f".//link[@name='left_lower_arm']/collision")
    left_lower_arm_collision.find('geometry').find('capsule').set('length', body_part_length[1])
    left_lower_arm_collision.find('geometry').find('capsule').set('radius', body_part_radius[1])
    root.find(f".//link[@name='left_lower_arm']/inertial").find('mass').set('value', body_part_mass[1])

    # Joint of left_lower_arm
    temp = round(float(body_part_length[1])/2 - 0.11500, 5)
    x = str(temp)
    y = '0.00000'
    z = '0.00000'
    # Collision element for the link
    root.find(f".//joint[@name='jointfix_12_37']").find('origin').set('xyz', f"{x} {y} {z}")

    # Collision element for the left_wristpalm
    left_wristpalm_collision = root.find(f".//link[@name='left_wristpalm']/collision")
    left_wristpalm_collision.find('geometry').find('capsule').set('length', body_part_length[2])
    left_wristpalm_collision.find('geometry').find('capsule').set('radius', body_part_radius[2])
    root.find(f".//link[@name='left_wristpalm']/inertial").find('mass').set('value', body_part_mass[2])

    # Joint of left_wrist
    temp = round(0.25 + float(body_part_length[1])/2 - 0.11500, 5)
    x = str(temp)
    y = '0.00000'
    z = '-0.04000'
    # Collision element for the link
    root.find(f".//joint[@name='left_wrist']").find('origin').set('xyz', f"{x} {y} {z}")

    # Collision element for the right_upper_arm
    right_upper_arm_collision = root.find(f".//link[@name='right_upper_arm']/collision")
    right_upper_arm_collision.find('geometry').find('capsule').set('length', body_part_length[3])
    right_upper_arm_collision.find('geometry').find('capsule').set('radius', body_part_radius[3])
    root.find(f".//link[@name='right_upper_arm']/inertial").find('mass').set('value', body_part_mass[3])

    # Joint of right_upper_arm
    x = '0.00000'
    y = '0.00000'
    temp = -round(float(body_part_length[3])/2 - 0.06, 5)
    z = str(temp)
    # Collision element for the link
    root.find(f".//joint[@name='jointfix_10_27']").find('origin').set('xyz', f"{x} {y} {z}")

    # Joint of right_elbow
    x = '0.03000'
    y = '0.00000'
    temp = -(round(0.2 + float(body_part_length[3])/2, 5) - 0.06)
    z = str(temp)
    # Collision element for the link
    root.find(f".//joint[@name='right_elbow']").find('origin').set('xyz', f"{x} {y} {z}")

    # Collision element for the right_lower_arm
    right_lower_arm_collision = root.find(f".//link[@name='right_lower_arm']/collision")
    right_lower_arm_collision.find('geometry').find('capsule').set('length', body_part_length[4])
    right_lower_arm_collision.find('geometry').find('capsule').set('radius', body_part_radius[4])
    root.find(f".//link[@name='right_lower_arm']/inertial").find('mass').set('value', body_part_mass[4])

    # Joint of right_lower_arm
    temp = round(float(body_part_length[4])/2 - 0.11500, 5)
    x = str(temp)
    y = '0.00000'
    z = '0.00000'
    # Collision element for the link
    root.find(f".//joint[@name='jointfix_9_29']").find('origin').set('xyz', f"{x} {y} {z}")

    # Collision element for the right_wristpalm
    right_wristpalm_collision = root.find(f".//link[@name='right_wristpalm']/collision")
    right_wristpalm_collision.find('geometry').find('capsule').set('length', body_part_length[5])
    right_wristpalm_collision.find('geometry').find('capsule').set('radius', body_part_radius[5])
    root.find(f".//link[@name='right_wristpalm']/inertial").find('mass').set('value', body_part_mass[5])

    # Joint of right_wrist
    temp = round(0.25 + float(body_part_length[4])/2 - 0.11500, 5)
    x = str(temp)
    y = '0.00000' 
    z = '-0.04000'
    # Collision element for the link
    root.find(f".//joint[@name='right_wrist']").find('origin').set('xyz', f"{x} {y} {z}")

    # Collision element for the left_thigh
    left_thigh_collision = root.find(f".//link[@name='left_thigh']/collision")
    left_thigh_collision.find('geometry').find('capsule').set('length', body_part_length[6])
    left_thigh_collision.find('geometry').find('capsule').set('radius', body_part_radius[6])
    left_thigh_collision.find('origin').set('xyz', '0.00000 -0.00500 ' + str(-float(body_part_length[6])/2))
    root.find(f".//link[@name='left_thigh']/inertial").find('mass').set('value', body_part_mass[6])

    # Collision element for the link
    root.find(f".//joint[@name='left_knee']").find('origin').set('xyz', '0.00000 -0.01000 ' + str(-(float(body_part_length[6]) + 0.04285)))

    # Collision element for the left_shin
    left_shin_collision = root.find(f".//link[@name='left_shin']/collision")
    left_shin_collision.find('geometry').find('capsule').set('length', body_part_length[7])
    left_shin_collision.find('geometry').find('capsule').set('radius', body_part_radius[7])
    left_shin_collision.find('origin').set('xyz', '0.00000 0.00000 ' + str(-float(body_part_length[7])/2))
    root.find(f".//link[@name='left_shin']/inertial").find('mass').set('value', body_part_mass[7])

    # Collision element for the link
    root.find(f".//joint[@name='left_ankle_y']").find('origin').set('xyz', '0.00000 0.00000 ' + str(-(float(body_part_length[7]) + 0.01)))

    # Collision element for the left_foot
    left_foot_collision = root.find(f".//link[@name='left_foot']/collision")
    left_foot_collision.find('geometry').find('capsule').set('length', body_part_length[8])
    left_foot_collision.find('geometry').find('capsule').set('radius', body_part_radius[8])
    root.find(f".//link[@name='left_foot']/inertial").find('mass').set('value', body_part_mass[8])

    # Collision element for the right_thigh
    right_thigh_collision = root.find(f".//link[@name='right_thigh']/collision")
    right_thigh_collision.find('geometry').find('capsule').set('length', body_part_length[9])
    right_thigh_collision.find('geometry').find('capsule').set('radius', body_part_radius[9])
    right_thigh_collision.find('origin').set('xyz', '0.00000 0.00500 ' + str(-float(body_part_length[9])/2))
    root.find(f".//link[@name='right_thigh']/inertial").find('mass').set('value', body_part_mass[9])

    # Collision element for the link
    root.find(f".//joint[@name='right_knee']").find('origin').set('xyz', '0.00000 0.01000 ' + str(-(float(body_part_length[9]) + 0.04285)))

    # Collision element for the right_shin
    right_shin_collision = root.find(f".//link[@name='right_shin']/collision")
    right_shin_collision.find('geometry').find('capsule').set('length', body_part_length[10])
    right_shin_collision.find('geometry').find('capsule').set('radius', body_part_radius[10])
    right_shin_collision.find('origin').set('xyz', '0.00000 0.00000 ' + str(-float(body_part_length[10])/2))
    root.find(f".//link[@name='right_shin']/inertial").find('mass').set('value', body_part_mass[10])

    # Collision element for the link
    root.find(f".//joint[@name='right_ankle_y']").find('origin').set('xyz', '0.00000 0.00000 ' + str(-(float(body_part_length[10]) + 0.01)))

    # Collision element for the right_foot
    right_foot_collision = root.find(f".//link[@name='right_foot']/collision")
    right_foot_collision.find('geometry').find('capsule').set('length', body_part_length[11])
    right_foot_collision.find('geometry').find('capsule').set('radius', body_part_radius[11])
    root.find(f".//link[@name='right_foot']/inertial").find('mass').set('value', body_part_mass[11])

    # Update the modified URDF file
    tree.write('./workers/' + str(urdf), pretty_print=True)

def set_fixed_legs(fixed, urdf = 'factory_worker.urdf'):
    # Parse the URDF file
    tree = ET.parse('./workers/' + str(urdf))
    root = tree.getroot()
    print(fixed)
    if(fixed):
        root.find(f".//joint[@name='abdomen_x']").set('type', 'fixed')
        root.find(f".//joint[@name='abdomen_y']").set('type', 'fixed')
        root.find(f".//joint[@name='abdomen_z']").set('type', 'fixed')

        root.find(f".//joint[@name='right_hip_x']").set('type', 'fixed')
        root.find(f".//joint[@name='right_hip_y']").set('type', 'fixed')
        root.find(f".//joint[@name='right_hip_z']").set('type', 'fixed')

        root.find(f".//joint[@name='left_hip_x']").set('type', 'fixed')
        root.find(f".//joint[@name='left_hip_y']").set('type', 'fixed')
        root.find(f".//joint[@name='left_hip_z']").set('type', 'fixed')

        root.find(f".//joint[@name='right_knee']").set('type', 'fixed')
        root.find(f".//joint[@name='left_knee']").set('type', 'fixed')

        root.find(f".//joint[@name='right_ankle_x']").set('type', 'fixed')
        root.find(f".//joint[@name='right_ankle_y']").set('type', 'fixed')

        root.find(f".//joint[@name='left_ankle_x']").set('type', 'fixed')
        root.find(f".//joint[@name='left_ankle_y']").set('type', 'fixed')
    else:
        root.find(f".//joint[@name='abdomen_x']").set('type', 'revolute')
        root.find(f".//joint[@name='abdomen_y']").set('type', 'revolute')
        root.find(f".//joint[@name='abdomen_z']").set('type', 'revolute')

        root.find(f".//joint[@name='right_hip_x']").set('type', 'revolute')
        root.find(f".//joint[@name='right_hip_y']").set('type', 'revolute')
        root.find(f".//joint[@name='right_hip_z']").set('type', 'revolute')

        root.find(f".//joint[@name='left_hip_x']").set('type', 'revolute')
        root.find(f".//joint[@name='left_hip_y']").set('type', 'revolute')
        root.find(f".//joint[@name='left_hip_z']").set('type', 'revolute')

        root.find(f".//joint[@name='right_knee']").set('type', 'revolute')
        root.find(f".//joint[@name='left_knee']").set('type', 'revolute')

        root.find(f".//joint[@name='right_ankle_x']").set('type', 'revolute')
        root.find(f".//joint[@name='right_ankle_y']").set('type', 'revolute')

        root.find(f".//joint[@name='left_ankle_x']").set('type', 'revolute')
        root.find(f".//joint[@name='left_ankle_y']").set('type', 'revolute')

    # Update the modified URDF file
    tree.write('./workers/' + str(urdf), pretty_print=True)