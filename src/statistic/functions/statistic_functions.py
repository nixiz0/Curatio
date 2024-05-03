from zipfile import ZipFile
from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from scipy.stats import shapiro
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from panel.forms import CSVUploadForm


def pca(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']

            # Read the contents of the CSV file using pandas 
            df = pd.read_csv(csv_file)

            # Select only numerical columns for PCA
            numeric_columns = df.select_dtypes(include=[np.number])

            # Standardize and scale the data
            scaler = StandardScaler()
            scaled_data = scaler.fit_transform(numeric_columns)

            # Create a PCA instance
            pca = PCA()

            # Fit the PCA model to the standardized data
            pca.fit(scaled_data)

            # Get explained variance
            explained_variance = pca.explained_variance_ratio_

            # Calculate cumulative explained variance
            cumulative_explained_variance = explained_variance.cumsum()

            # Create a 1x2 grid of subplots
            fig, axes = plt.subplots(1, 2, figsize=(12, 6))

            # Plot the cumulative explained variance curve in the first subplot
            axes[0].scatter(range(1, len(cumulative_explained_variance) + 1), cumulative_explained_variance, marker='o')
            axes[0].plot(range(1, len(cumulative_explained_variance) + 1), cumulative_explained_variance, linestyle='--')
            axes[0].set_xlabel('Number of principal components')
            axes[0].set_ylabel('Cumulative explained variance')
            axes[0].set_title('Cumulative explained variance by principal component')

            # Calculate the loadings (vecteurs propres)
            loadings = pca.components_.T  # Transpose for easy use

            # Plot the correlation circle in the second subplot
            num_pc = len(pca.explained_variance_ratio_)
            for i in range(num_pc):
                axes[1].arrow(0, 0, loadings[i, 0], loadings[i, 1], head_width=0.03, head_length=0.05, fc='r', ec='r')
                axes[1].text(loadings[i, 0]*1.2, loadings[i, 1]*1.2, numeric_columns.columns[i], color='b', ha='center', va='center')

            # Add a unit circle to the second subplot
            circle = plt.Circle((0, 0), 1, color='b', fill=False)
            axes[1].add_artist(circle)

            axes[1].grid()
            axes[1].set_aspect('equal', adjustable='box')
            axes[1].set_xlim(-1, 1)
            axes[1].set_ylim(-1, 1)
            axes[1].set_xlabel('PC1')
            axes[1].set_ylabel('PC2')
            axes[1].set_title('Correlation Circle')

            # Save the PCA plot to BytesIO
            img_pca = BytesIO()
            plt.savefig(img_pca, format='png')
            plt.close()

            # Plot the explained variance ratio bar chart with curve
            plt.figure(figsize=(10, 6))
            plt.bar(range(1, len(explained_variance) + 1), explained_variance, label='Individual Explained Variance')
            plt.plot(range(1, len(cumulative_explained_variance) + 1), cumulative_explained_variance, label='Cumulative Explained Variance', marker='o')
            plt.xlabel('Principal Component')
            plt.ylabel('Explained Variance Ratio')
            plt.title('Explained Variance Ratio for Principal Components')
            plt.legend()
            plt.tight_layout()

            # Save the explained variance ratio plot to BytesIO
            img_var_ratio = BytesIO()
            plt.savefig(img_var_ratio, format='png')
            plt.close()

            # Combine the images into a single response
            img_combined = BytesIO()
            with ZipFile(img_combined, 'w') as zipf:
                zipf.writestr('pca_analysis.png', img_pca.getvalue())
                zipf.writestr('explained_variance_ratio.png', img_var_ratio.getvalue())

            # Create a response with the combined images
            response_combined = HttpResponse(img_combined.getvalue(), content_type='application/zip')
            response_combined['Content-Disposition'] = 'attachment; filename=combined_images.zip'

            return response_combined
    else:
        form = CSVUploadForm()
    return render(request, 'csv_statistic/statistic_functions/pca.html', {'form': form})


def chi_square(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column1 = form.cleaned_data['column']
            column2 = form.cleaned_data['column2']

            # Read the contents of the CSV file using pandas
            df = pd.read_csv(csv_file)

            # Specify the categorical columns you want to compare
            categorical_column1 = column1
            categorical_column2 = column2

            # Create a contingency table
            contingency_table = pd.crosstab(df[categorical_column1], df[categorical_column2])

            # Use the chi-square test function
            chi2_stat, p_value, degrees_of_freedom, expected_data = chi2_contingency(contingency_table)

            # Display the results on a graph
            fig, axes = plt.subplots(1, 2, figsize=(20, 12))

            # Graph of observed frequencies
            contingency_table.plot(kind='bar', ax=axes[0])
            axes[0].set_title('Observed Frequencies')
            axes[0].set_xlabel(categorical_column1)
            axes[0].set_ylabel('Frequency')

            # Graph of expected frequencies
            pd.DataFrame(expected_data, index=contingency_table.index, columns=contingency_table.columns).plot(kind='bar', ax=axes[1])
            axes[1].set_title('Expected Frequencies')
            axes[1].set_xlabel(categorical_column1)
            axes[1].set_ylabel('Frequency')

            # Add legends beside the graphs
            axes[0].legend(loc='upper right')
            axes[1].legend(loc='upper right')

            # Save the graphs into BytesIO
            img_observed = BytesIO()
            img_expected = BytesIO()

            plt.savefig(img_observed, format='png')
            plt.close()

            pd.DataFrame(expected_data, index=contingency_table.index, columns=contingency_table.columns).plot(kind='bar').get_figure().savefig(img_expected, format='png')
            plt.close()

            # Create a response with the combined images
            response = HttpResponse(img_observed.getvalue(), content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename=observed_frequencies.png'

            # Return the response
            return response
    else:
        form = CSVUploadForm()
    return render(request, 'csv_statistic/statistic_functions/chi_square.html', {'form': form})


def shapiro_wilk(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']

            # Read the contents of the CSV file using pandas
            df = pd.read_csv(csv_file)

            # Create an empty list to store the results
            results = []

            # Loop through the numeric columns of the DataFrame
            for column in df.select_dtypes(include='number').columns:
                # Perform the Shapiro-Wilk test
                stat, p_value = shapiro(df[column])

                # Determine if the distribution is normal based on the p-value
                is_normal = p_value > 0.05

                # Add the results to the list
                results.append({
                    'Variable': column,
                    'Test Statistic': stat,
                    'P-Value': p_value,
                    'Normal Distribution': is_normal
                })

            # Create a DataFrame from the list of results
            results_df = pd.DataFrame(results)

            # Create a plot of the results
            plt.figure(figsize=(10, 6))
            plt.bar(results_df['Variable'], results_df['P-Value'], color=results_df['Normal Distribution'].map({True: 'green', False: 'red'}))
            plt.title('Shapiro-Wilk Test Results')
            plt.xlabel('Variable')
            plt.ylabel('P-Value')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()

            # Save the plot as a PNG image
            img_observed = BytesIO()
            plt.savefig(img_observed, format='png')
            plt.close()

            # Create a response with the saved image
            response = HttpResponse(img_observed.getvalue(), content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename=shapiro_wilk_results.png'

            # Return the response
            return response
    else:
        form = CSVUploadForm()
    return render(request, 'csv_statistic/statistic_functions/shapiro_wilk.html', {'form': form})


def features_importance(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column = form.cleaned_data['column']

            # Read the contents of the CSV file using pandas
            df = pd.read_csv(csv_file)

            # Standardize the data
            scaler = StandardScaler()
            df_scaled = pd.DataFrame(scaler.fit_transform(df.select_dtypes(include='number')), columns=df.select_dtypes(include='number').columns)

            # Separate features and target variable
            X = df_scaled.drop(column, axis=1)
            y = df[column]

            # Create a random forest classifier
            clf = RandomForestClassifier(n_estimators=100)

            # Fit the model
            clf.fit(X, y)

            # Get feature importances
            feature_importances = clf.feature_importances_

            # Create a DataFrame from feature importances
            feature_importance_df = pd.DataFrame({
                'Variable': X.columns,
                'Importance': feature_importances
            })

            # Sort the DataFrame by importance in descending order
            feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

            # Select the top 50 features
            top_features = feature_importance_df.head(50)

            # Create a plot of the top 50 feature importances
            plt.figure(figsize=(15, 8))  # Adjust the figure size if needed
            plt.bar(top_features['Variable'], top_features['Importance'], color='blue')
            plt.title('Top 50 Feature Importance Analysis')
            plt.xlabel('Variable')
            plt.ylabel('Importance')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()

            # Save the plot as a PNG image
            img_observed = BytesIO()
            plt.savefig(img_observed, format='png')
            plt.close()

            # Create a response with the saved image
            response = HttpResponse(img_observed.getvalue(), content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename=feature_importance_analysis.png'

            # Return the response
            return response
    else:
        form = CSVUploadForm()
    return render(request, 'csv_statistic/statistic_functions/features_importance.html', {'form': form})