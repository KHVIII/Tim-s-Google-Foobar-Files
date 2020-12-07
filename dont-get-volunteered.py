
def solution (src, dest):
    start_coord = (src % 8, 7 - (src //8))
    end_coord = (dest % 8, 7 - (dest //8))
    existing_move_dict = {} #global dict so no nodes are repeated

    def generate_next(coord,dest_coord): #generate a list of next legal moves
        x_coord,y_coord = coord
        pos_steps = [(1,2),(-1,2),(-1,-2),(1,-2),(2,1),(-2,1),(-2,-1),(1,2)]
        aval_next_pos_lst = []
        
        for (x_change,y_change) in pos_steps:
            #print('test',(x_change,y_change,x_coord,y_coord))
            pos_x_coord = x_coord + x_change
            pos_y_coord = y_coord + y_change
            #print('test2',(pos_x_coord,pos_y_coord))
            if pos_x_coord >= 0 and pos_x_coord <= 7 and pos_y_coord >=0 and pos_y_coord <= 7 and (pos_x_coord,pos_y_coord) not in existing_move_dict: #check the move is legal or not
                aval_next_pos_lst.append ( (pos_x_coord,pos_y_coord) )
                existing_move_dict[(pos_x_coord,pos_y_coord)] = None
                if (pos_x_coord,pos_y_coord) == dest_coord:
                    break;

        return aval_next_pos_lst



    #breadth-first approach recursive search by each layer
    def solution_helper_two(curr_layer_lst,dest_coord):
        for coord in curr_layer_lst:
            if coord == dest_coord:
                return 0

        next_layer_lst = []
        for coord in curr_layer_lst:
            next_layer_lst.extend(generate_next(coord,dest_coord))
        return solution_helper_two(next_layer_lst,dest_coord) + 1;
            

    return solution_helper_two([start_coord],end_coord)
    

        
        
    
