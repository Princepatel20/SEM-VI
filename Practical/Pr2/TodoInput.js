import React from 'react'

import { name,age } from './moduledemo'

export default function TodoInput() {

return (

<div>

<button onClick={() => alert(`Hello ${name} is ${age} old `)}>

Click
</button>

</div>

)

}
