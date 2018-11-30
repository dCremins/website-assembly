import React, {Component} from 'react'
import PropTypes from 'prop-types';
/**
* This is a test. This is only a test.
*/
export default class Test extends Component {
  render() {
    const {value} = this.props;

    return (
      <div>
        <input value={value} />
      </div>
    )
  }
}

Test.propTypes = {
    /**
     * The value displayed in the input
     */
    value: PropTypes.string
}
