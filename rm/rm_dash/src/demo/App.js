/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import Test from '../lib'

class App extends Component {

    constructor() {
        super();
        this.state = {
            value: ''
        };
    }

    render() {
        return (
            <div>
              <Test value={this.state.value} />
            </div>
        )
    }
}

export default App;
