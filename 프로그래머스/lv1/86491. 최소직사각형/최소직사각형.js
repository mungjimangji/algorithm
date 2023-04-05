function solution(sizes) {
//     filter
  const max = Array.from({ length: 2 }, () => Number.MIN_SAFE_INTEGER);
    
  const rotateArr = sizes.map(size => {
     return size[1] > size[0] ? [size[1], size[0]] : [size[0], size[1]]
  });

    for(let i = 0; i < rotateArr.length; i++) {
        if(rotateArr[i][0] > max[0]) max[0] = rotateArr[i][0]
        if(rotateArr[i][1] > max[1]) max[1] = rotateArr[i][1]
    }

    return max[0] * max[1]
}
