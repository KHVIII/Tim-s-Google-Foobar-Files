import collections

def solution (src, dest):
    start_coord = (src % 8, 7 - (src //8))
    end_coord = (dest % 8, 7 - (dest //8))
    existing_move_dict = {}
    print ('og_coords',start_coord,end_coord)
    def generate_next(coord,dest_coord):
        x_coord,y_coord = coord
        pos_steps = [(1,2),(-1,2),(-1,-2),(1,-2),(2,1),(-2,1),(-2,-1),(1,2)]
        aval_next_pos_lst = []
        
        for (x_change,y_change) in pos_steps:
            #print('ha',(x_change,y_change,x_coord,y_coord))
            pos_x_coord = x_coord + x_change
            pos_y_coord = y_coord + y_change
            #print('haha',(pos_x_coord,pos_y_coord))
            if pos_x_coord >= 0 and pos_x_coord <= 7 and pos_y_coord >=0 and pos_y_coord <= 7 and (pos_x_coord,pos_y_coord) not in existing_move_dict:
                aval_next_pos_lst.append ( (pos_x_coord,pos_y_coord) )
                existing_move_dict[(pos_x_coord,pos_y_coord)] = None
                aval_next_pos_lst.append
                if (pos_x_coord,pos_y_coord) == dest_coord:
                    break;

        return aval_next_pos_lst


    
##    def solution_helper (src_coord, dest_coord):
##        if src_coord == dest_coord:
##            return 0;
##        next_pos_lst = generate_next(src_coord) #get a list of legal next moves
##
##
##
##
##            #if current next step have no solutions
##        steps_list = []
##        next_level = []
##        for next_pos_coords in next_pos_lst:
##            if next_pos_coords in existing_move_dict:
##                steps_taken = existing_move_dict[next_pos_coords] + 1;
##            else:
##                next_level.append(next_pos_coords)
##            steps_list.append(steps_taken + 1);
##        for aa in next_level:
##            steps_taken = solution_helper(aa,dest_coord) + 1
##         existing_move_dict[next_pos_coords]= min(steps_list);
##         return existing_move_dict[next_pos_coords]


    def solution_helper_two(curr_layer_lst,dest_coord):
        for coord in curr_layer_lst:
            if coord == dest_coord:
                return 0

        next_layer_lst = collections.deque()
        for coord in curr_layer_lst:
            next_layer_lst.extend(generate_next(coord,dest_coord))
        return solution_helper_two(next_layer_lst,dest_coord) + 1;
            

    return solution_helper_two([start_coord],end_coord)
    

        
        
    
