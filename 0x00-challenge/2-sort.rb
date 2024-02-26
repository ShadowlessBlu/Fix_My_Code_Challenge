###
#
#  Sort integer arguments (ascending) 
#
###

res = []
ARGV.each do |arg|
    # skip if not integer
    next if arg !~ /^-?[0-9]+$/

    # convert to integer
    i_arg = arg.to_i
    
    # insert result at the right position
    is_inserted = false
    i = 0
    l = res.size
    while !is_inserted && i < l do
        if res[i] < i_arg
            i += 1
        else
            res.insert(i, i_arg)
            is_inserted = true
            break
        end
    end
    res << i_arg if !is_inserted
end

puts res
