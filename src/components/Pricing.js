import * as React from "react";
import PropTypes from "prop-types";

const Pricing = ({ data }) => (
  <div className="columns">
    {data.map((price) => (
      <div key={price.plan} className="column unit">
          <h2 className="is-size-1 has-text-weight-bold has-text-primary has-text-centered">
            {price.plan}
          </h2>
          <h3 className="has-text-centered">
            {price.price} year olds
          </h3>
          <p className="has-text-centered lead">Meeting time:<br />{price.description}</p>
      </div>
    ))}
  </div>
);

Pricing.propTypes = {
  data: PropTypes.arrayOf(
    PropTypes.shape({
      plan: PropTypes.string,
      price: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
      description: PropTypes.string,
      items: PropTypes.array,
    })
  ),
};

export default Pricing;
